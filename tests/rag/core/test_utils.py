"""
Test all helper function.
"""

from src.rag.core.enums import HashAlgorithms
from src.rag.core.utils import generate_id


TEST_ARGS = ["param1", "param2"]


def test_generate_id_md5():
    expected_out = "4e6b6d3abf29646dc354278eb3084b88"
    func_out = generate_id(HashAlgorithms.md5, *TEST_ARGS)
    assert expected_out == func_out


def test_generate_id_sha256():
    expected_out = "d2f80f2ad565ba438cb875628cca0481f814c593aec00fa38deda5fdcb917a38"
    func_out = generate_id(HashAlgorithms.sha256, *TEST_ARGS)
    assert expected_out == func_out


def test_generate_id_sha512():
    expected_out = "917b1172caace06cbcebc681be4bcb03e82c2a4fa27a9e9f645f445f935104642204d55f83fbf9ffddfabd2f31f27a95daa54665399877a53667eff105f81897"
    func_out = generate_id(HashAlgorithms.sha512, *TEST_ARGS)
    assert expected_out == func_out


def test_generate_id_unknow_algorithm():
    expected_out = None
    func_out = generate_id("Unknow hash algorithm", *TEST_ARGS)
    assert expected_out == func_out
