def isPalindrome(s: str) -> bool:
    new_str = s
    for c in s:
        if not(c.isalpha() or c.isdigit()) : # 숫자나 문자가 아니라면
            new_str = new_str.replace(c, "") # c 값을 공백으로 바꾸기

    repeat = len(new_str)//2
    new_str = new_str.lower()

    for i in range(repeat):
        if new_str[i] is not new_str[len(new_str)-1-i]:
            return False

    return True










