# 사용자로부터 월급을 입력 받아 다음과 같이 공제 세액을 계산해 출력해
# 주는 함수를 정의하고 테스트 하시오.
# 단, 함수 이름은 sal_amount() 로 하시오.

# 아래와 같이 호출하여 함수를 실행
# sal_amount()

# 프로그램 실행화면

# 월급을 입력해 주세요 : >? 2400000
# 월 급여 :  2400000
#  [소득 공제액]
# 국민 연금 :  108000.0
# 건강 보험 :  73440.0
# 장기 요양 :  4810.320000000001
# 고용 보험 :  15600.0
# 소 득 세 :  33570
# 지방소득세 :  3357.0
# 총     공제액 :  238777.32
#  05. 함수와 람다
# ========================================
# 실 수 령 액 :  2161222.68

def sal_amount():

    salary = int(input("월급을 입력해 주세요 : >? "))

    national_pension = salary * 0.045
    health_insurance = salary * 0.0306
    long_term_care = health_insurance * 0.0655
    employment_insurance = salary * 0.0065

    income_tax = 33570

    local_income_tax = income_tax * 0.1

    total_deductions = (national_pension + health_insurance + long_term_care +
                        employment_insurance + income_tax + local_income_tax)

    net_salary = salary - total_deductions

    print(f"\n월 급여 :  {salary}")
    print(f"[소득 공제액]")
    print(f"국민 연금 :  {national_pension:.1f}")
    print(f"건강 보험 :  {health_insurance:.1f}")
    print(f"장기 요양 :  {long_term_care:.12f}")
    print(f"고용 보험 :  {employment_insurance:.1f}")
    print(f"소 득 세 :  {income_tax:.0f}")
    print(f"지방소득세 :  {local_income_tax:.1f}")
    print(f"총    공제액 :  {total_deductions:.2f}")
    print("="*40)
    print(f"실 수 령 액 :  {net_salary:.2f}")

sal_amount()
