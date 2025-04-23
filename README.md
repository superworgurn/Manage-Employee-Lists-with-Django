# ระบบจัดการรายชื่อผู้สมัครงาน (Job Application Management System)

[![ภาษา](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/) [![เฟรมเวิร์ก](https://img.shields.io/badge/framework-Django-green.svg)](https://www.djangoproject.com/) 

โปรเจกต์นี้เป็นเว็บแอปพลิเคชันสำหรับจัดการรายชื่อ และ ข้อมูลของผู้สมัครงาน พัฒนาด้วย Django Framework ช่วยให้ฝ่ายบุคคล (HR) หรือ ผู้ที่เกี่ยวข้องสามารถติดตาม และ จัดการกระบวนการรับสมัครงานได้อย่างเป็นระบบ และ มีประสิทธิภาพ

## ✨ คุณสมบัติหลัก (Features)

* **เพิ่มข้อมูลผู้สมัคร (Add Applicant):** บันทึกข้อมูลส่วนตัว, ประสบการณ์ทำงาน และ ตำแหน่งที่สมัคร
* **ลบข้อมูลผู้สมัคร (Delete Applicant):** ลบข้อมูลผู้สมัครที่ไม่ต้องการออกจากระบบ
* **แก้ไขข้อมูลผู้สมัคร (Edit Applicant):** อัปเดตข้อมูลของผู้สมัครเมื่อมีการเปลี่ยนแปลง
* **ค้นหาผู้สมัคร (Search Applicant):** ค้นหาผู้สมัครได้อย่างรวดเร็วจากชื่อ, ตำแหน่งงานที่สมัคร
* **แสดงสถานะการสมัครงาน (Display Application Status):** ติดตามสถานะของผู้สมัครแต่ละคน (เช่น รอสัมภาษณ์,สัมภาษณ์แล้ว,รับงานแล้ว,ไม่ผ่าน)


## 🛠️ เทคโนโลยีที่ใช้ (Technologies Used)

* **Backend:** Python, Django Framework
* **Database:** SQLite (ค่าเริ่มต้นของ Django) 
* **Frontend:** HTML, CSS, Bootstrap 


## 🚀 การติดตั้งและเริ่มใช้งาน (Installation and Setup)

1.  **Clone a Repository:**
 ```bash
git clone https://github.com/superworgurn/Manage-Employee-Lists-with-Django.git
cd judy
```
2.  **สำหรับเข้าหน้า Admin:**
   ```bash
    User judy
    Password judy12345678
   ```
3.  **สำหรับการใช้งาน**
 ```bash
  python manage.py runserver
 ```

4.  เปิดเว็บเบราว์เซอร์แล้วไปที่ `http://127.0.0.1:8000/` เพื่อดูแอปพลิเคชัน
5.  เข้าหน้า Admin ได้ที่ `http://127.0.0.1:8000/admin/`

## ใช้งาน (Usage)

* เข้าสู่ระบบด้วยบัญชีที่คุณสร้างขึ้น (หรือเข้าหน้า Admin ด้วย Superuser)
* ไปยังหน้าจัดการผู้สมัครเพื่อเริ่ม เพิ่ม, ลบ, แก้ไข, ค้นหา หรือดูสถานะของผู้สมัคร

## 🖼️ ตัวอย่างหน้าจอ (Screenshots)

![enter image description here](https://github.com/superworgurn/Manage-Employee-Lists-with-Django/blob/main/Screenshot.png?raw=true)

## สมาชิกกลุ่ม
 1. 67152363 นาย ธนาธิป คำมุงคุล
 2. 67140388 อนุสรณ์ ชอบทำกิจ
 3. 67141977 วรกันต์ รื่นพิทักษ์

## 🤝 การมีส่วนร่วม (Contributing)

หากคุณต้องการมีส่วนร่วมในการพัฒนาโปรเจกต์นี้ สามารถทำตามขั้นตอนดังนี้:

1.  Fork โปรเจกต์นี้
2.  สร้าง Branch ใหม่ (`git checkout -b feature/ชื่อฟีเจอร์ใหม่`)
3.  Commit การเปลี่ยนแปลงของคุณ (`git commit -m 'เพิ่มฟีเจอร์: ชื่อฟีเจอร์ใหม่'`)
4.  Push ไปยัง Branch (`git push origin feature/ชื่อฟีเจอร์ใหม่`)
5.  เปิด Pull Request
