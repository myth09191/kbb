import random
def get_choice(choice):
    if choice == "1":
        return "Búa"
    elif choice == "2":
        return "Bao"
    elif choice == "3":
        return "Kéo"
    else:
        return "Not a valid choice"

def main():
    print("Kéo Búa Bao Battle")
    print("[1]=Búa, [2]=Bao, [3]=Kéo and [Q]=Thoát game")

    choices = ["1", "2", "3"]
    counter = 1
    game_on = True

    while game_on:
        user_choice = input(f"Game #{counter}. Chọn chiêu thức: ")
        user_choice = user_choice.upper()

        if user_choice == "Q":
            print('Sợ chạy à :)')
            game_on = False
        else:
            random_index = random.randint(0,2)
            computer_choice = choices[random_index]

            print(f"Bạn tung ra skill {get_choice(user_choice)} VS kẻ thù {get_choice(computer_choice)}")
            
            #Winning Rules:
            if user_choice == "1" and computer_choice == "3":
                print('Chúc mừng, bạn đã cho nó ăn búa. Búa đập hư kéo')
            elif user_choice == "2" and computer_choice == "1":
                print('Chúc mừng, bạn đã thu búa của nó. Bao chùm búa')
            elif user_choice == "3" and computer_choice == "2":
                print('Chúc mừng, bạn đã cắt bao của nó. Kéo cắt bao thành 2 mảnh')
            elif user_choice == "1" and computer_choice == "2":
                print('Ngu, bị đánh te tua. Bao chùm búa')
            elif user_choice == "3" and computer_choice == "1":
                print('Ngu, bị đánh te tua. Búa đập hư kéo')
            elif user_choice == "2" and computer_choice == "3":
                print('Ngu, bị đánh te tua. Kéo cắt bao thành 2 mảnh')
            elif user_choice == computer_choice:
                print(f"Bất phân thắng bại đại chiến thêm 300 hiệp! {get_choice(user_choice)}")
            else:
                print('Chưa học skill! chọn 1 2 3 Q')

            counter+=1
        print("-"*40)
    
if __name__ == "__main__":
    main()