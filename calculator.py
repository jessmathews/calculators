def main():
    while True:
        op = input("Enter the operator:").strip()
        
        if (op =='+' or op =='-' or op =='*' or op =='/' or op =='%'):
            nums = input("Enter two numbers:").split()
            nums = [int(x) for x in nums]

            if op =='+':
                ans = nums[0] + nums[1]
                print(ans)

            if op =='-':
                ans = nums[0] - nums[1]
                print(ans)

            if op =='*':
                ans = nums[0] * nums[1]
                print(ans)

            if op =='/':
                ans = nums[0] / nums[1]
                print(ans)

            if op == '%':
                ans = nums[0] % nums[1]
                print(ans)

        elif (op =='x' or op =='X'):
            print("Bye...")
            exit()
        else:
            print("Invalid Operation!")
main()