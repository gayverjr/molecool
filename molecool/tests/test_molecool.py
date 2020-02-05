"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys
import numpy as np

def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules

def test_calculate_distance():
    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])
    calculated_distance = molecool.calculate_distance(r1,r2)
    expected_dist = 1.0
    assert calculated_distance == expected_dist 

@pytest.mark.parametrize("p1,p2,p3,expected_angle",[(np.array([np.sqrt(2)/2,np.sqrt(2)/2,0]),
                                                    np.array([0,0,0]),
                                                    np.array([1,0,0]),
                                                    45),
                                                    (np.array([0,0,-1]),
                                                     np.array([0,1,0]),
                                                     np.array([1,0,0]),
                                                     60 
                                                    )])
def test_calculate_angle(p1,p2,p3,expected_angle):
    calc_angle = molecool.calculate_angle(p1,p2,p3,degrees=True)
    assert calc_angle == pytest.approx(expected_angle)



