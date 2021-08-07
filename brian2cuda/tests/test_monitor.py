from nose import with_setup
from nose.plugins.attrib import attr

from numpy.testing import assert_equal
from brian2 import *
from brian2.devices.device import reinit_and_delete


@attr('cuda_standalone', 'standalone-only')
@with_setup(teardown=reinit_and_delete)
def test_state_monitor_more_threads_than_single_block():
    # Currently, statemonitor only works for <=1024 recorded variables (#201).
    # This is a test is to remind us of the issue.
    G = NeuronGroup(1025, 'v:1')
    mon = StateMonitor(G, 'v', record=True)

    run(defaultclock.dt)

    assert_equal(mon.v, 0)


if __name__ == '__main__':
    import brian2cuda
    set_device('cuda_standalone', directory=None)
    test_state_monitor_more_threads_than_single_block()
