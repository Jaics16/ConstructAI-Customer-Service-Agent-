from company_info import company_info


def test_company_info():
    print("\nTest 1: Company information")
    print(company_info("all"))

    print("\nTest 2: Services")
    print(company_info("services"))

    print("\nTest 3: Location")
    print(company_info("location"))

    print("\nTest 4: Unknown topic")
    print(company_info("unknown_test_topic"))


if __name__ == "__main__":
    test_company_info()