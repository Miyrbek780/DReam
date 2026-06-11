students = []

def add_student():
    name = input("Talaba ismini kiriting: ").strip()
    age = input("Yoshini kiriting: ").strip()
    course = input("Kursini kiriting: ").strip()

    # Kurs kiritishda xato ketmasligi uchun tekshiramiz
    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Talaba muvaffaqiyatli qo'shildi!\n")

def view_students():
    if not students: # len(students) == 0 bilan bir xil, lekin qisqaroq va toza
        print("Talabalar mavjud emas.\n")
    else:
        print("\nTalabalar ro'yxati:")
        for index, student in enumerate(students, start=1):
            print(f"{index}. {student['name']} - {student['age']} yosh - {student['course']}-kurs")
        print() 

def search_student():
    search_name = input("Qidirilayotgan talaba ismini kiriting: ").strip()
    found = False

    for student in students:
        if student['name'].lower() == search_name.lower():
            print(f"\nTalaba topildi:")
            print(f"Ismi: {student['name']}, Yoshi: {student['age']}, Kursi: {student['course']}\n")
            found = True
            break 
            
    if not found:
        print("Talaba topilmadi.\n")

def delete_student():
    name = input("O'chiriladigan talaba ismini kiriting: ").strip()
    found = False
    
    # Ro'yxatdan elementni xavfsiz o'chirish
    for student in students:
        if student['name'].lower() == name.lower():
            students.remove(student)
            print("Talaba muvaffaqiyatli o'chirildi!\n")
            found = True
            break
            
    if not found:
        print("Bunday ismli talaba topilmadi.\n")

# Dastur menyusi
while True:
    print("--- Talabalar Tizimi ---")
    print("1. Talaba qo'shish")
    print("2. Talabalarni ko'rish")
    print("3. Talabani qidirish")
    print("4. Talabani o'chirish")
    print("5. Chiqish")
    
    tanlov = input("Xizmat turini tanlang (1-5): ").strip()
    
    if tanlov == '1':
        add_student()
    elif tanlov == '2':
        view_students()
    elif tanlov == '3':
        search_student()
    elif tanlov == '4':
        delete_student()
    elif tanlov == '5':
        print("Dastur tugatildi.")
        break
    else:
        print("Noto'g'ri buyruq kiritildi!\n")
        
