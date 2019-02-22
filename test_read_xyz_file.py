from unittest import TestCase
import pytest

from dimensionality_reduction_functions import *

class Test_read_xyz_file(TestCase):

    def test_oneline(self):
        name, energies, atoms, coordinates = read_xyz_file('unittests/oneline.xyz')
        assert len(atoms) == 1
        assert coordinates.shape == (1,1,3)

    def test_twolines(self):
        name, energies, atoms, coordinates = read_xyz_file('unittests/twolines.xyz')
        assert len(atoms) == 2
        assert coordinates.shape == (1,2,3)

    def test_twoframes(self):
        name, energies, atoms, coordinates = read_xyz_file('unittests/twoframes.xyz')
        assert len(atoms) == 1
        assert coordinates.shape == (2,1,3)

    def test_comment(self):
        with pytest.raises(Exception):
            name, energies, atoms, coordinates = read_xyz_file('unittests/comment.xyz')

    def test_extra_data(self):
        name, energies, atoms, coordinates = read_xyz_file('unittests/extradata.xyz')
        assert coordinates[1,1] == (1.0, 1.0, 1.0)

    def test_incorrect_atom_count(self):
        with pytest.raises(Exception):
            read_xyz_file('unittests/incorrectatomcount.xyz')

    def test_missing_coordinate(self):
        with pytest.raises(Exception):
            read_xyz_file('unittests/missingcoordinate.xyz')

    def test_missing_element(self):
        with pytest.raises(Exception):
            read_xyz_file('unittests/missingelement.xyz')
