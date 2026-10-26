
"""
Test file for Kerala BuildCare company information.
Save as: test_company_info.py
"""

from pprint import pprint

# Change "main" to your actual Python filename (without .py)
from main import company_info


def test_company_information():
    print("\n=== Test 1: All company information ===")
    result = company_info("all")
    pprint(result)

    assert result.get("found") is True, "Company information was not found!"
    assert "company_name" in result, "Company name is missing!"
    assert "location" in result, "Company location is missing!"
    assert "services" in result, "Company services are missing!"

    print("PASS: Company information retrieved successfully.")


def test_services():
    print("\n=== Test 2: Services lookup ===")
    result = company_info("services")
    pprint(result)

    assert result.get("found") is True, "Services were not found!"
    print("PASS: Services lookup works.")


def test_location():
    print("\n=== Test 3: Location lookup ===")
    result = company_info("location")
    pprint(result)

    assert result.get("found") is True, "Location was not found!"
    print("PASS: Location lookup works.")


def test_unknown_topic():
    print("\n=== Test 4: Unknown topic ===")
    result = company_info("unknown_test_topic")
    pprint(result)

    assert result.get("found") is False, "Unknown topic should not be found!"
    print("PASS: Unknown topics are handled correctly.")


if __name__ == "__main__":
    tests = [
        test_company_information,
        test_services,
        test_location,
        test_unknown_topic,
    ]

    passed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as error:
            print(f"FAIL: {test.__name__}: {error}")

    print(f"\n=== RESULTS: {passed}/{len(tests)} tests passed ===")
