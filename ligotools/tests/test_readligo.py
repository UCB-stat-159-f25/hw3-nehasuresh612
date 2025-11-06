import pytest
import readligo as rl
import numpy as np

def test_dq_channel_to_seglist():
    # create a channel that starts and ends with 1 hz and has 
    dq = np.array([1, 1, 0, 0, 1, 1, 1])
    seglist = rl.dq_channel_to_seglist(dq, fs=1)

    # expected outputs 
    expected = [slice(0, 2), slice(4, 7)]

    # assert correct dimensions 
    assert len(seglist) == len(expected)

    # assert correct values in seglist expected and observed
    for s, e in zip(seglist, expected):
        assert s.start == e.start and s.stop == e.stop

def test_segmentlist_class():
    # create a toy example of 2 segments representing ligo data
    toy_segments = [(100, 200), (300, 400)]
    seglist = rl.SegmentList(toy_segments)
    
    # test that the .seglist attribute is stored like list(zip(start, stop))
    assert seglist.seglist == toy_segments

    # check that string representation from __repr__ magic method
    text_repr = repr(seglist)
    assert "SegmentList" in text_repr and "100" in text_repr

    # make sure we can loop over it like a normal list
    starts = [s[0] for s in seglist]
    assert starts == [100, 300]