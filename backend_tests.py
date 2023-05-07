import json
from backend_code import OptiBizBackend


def test_validate_inputs():
    optibiz_backend = OptiBizBackend()
    valid_data = {"key": "value"}
    invalid_data = {"key": 123}
    assert optibiz_backend.validate_inputs(valid_data) == True
    assert optibiz_backend.validate_inputs(invalid_data) == False


def test_separate_concerns():
    optibiz_backend = OptiBizBackend()
    assert optibiz_backend.separate_concerns() == "Concerns separated"


def test_health_check():
    optibiz_backend = OptiBizBackend()
    assert optibiz_backend.health_check() == "Healthy"


def test_versioning():
    optibiz_backend = OptiBizBackend()
    assert optibiz_backend.versioning() == "Version 1.0.0"


def test_write_tests():
    optibiz_backend = OptiBizBackend()
    assert optibiz_backend.write_tests() == "Tests written"


if __name__ == '__main__':
    test_validate_inputs()
    test_separate_concerns()
    test_health_check()
    test_versioning()
    test_write_tests()