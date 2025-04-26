from django.db import models

# Create your models here.
class person(models.Model):
    # Dropdown สถานะการสมัครงาน
    STATUS_CHOICES = [
        ('waiting','รอสัมภาษณ์'),
        ('interviewed','สัมภาษณ์แล้ว'),
        ('hired','รับงานแล้ว'),
        ('not_passed','ไม่ผ่าน'),
    ]

    # Dropdown ตำแหน่งงาน (รูปแบบที่ถูกต้องสำหรับ Django choices)
    POSITION_CHOICES = [
    ('UX/UI Designer', 'UX/UI Designer'),
    ('Software Developer/Engineer', 'Software Developer/Engineer'),
    ('Data Scientist', 'Data Scientist'),
    ('Cybersecurity Analyst', 'Cybersecurity Analyst'),
    ('Cloud Engineer/Architect', 'Cloud Engineer/Architect'),
    ('DevOps Engineer', 'DevOps Engineer'),
    ('Network Engineer', 'Network Engineer'),
    ('IT Project Manager', 'IT Project Manager'),
    ('Database Administrator (DBA)', 'Database Administrator (DBA)'),
]

# รับข้อมูล + แก้ไขข้อมูล
    first_name = models.CharField("ชื่อ (First_name)",max_length=100)
    last_name = models.CharField("นามสกุล (Last_name)",max_length=100)
    gmail = models.EmailField("อีเมล (Gmail)")
    phone_number = models.CharField("เบอร์โทรศัพท์ (Phone_number)",max_length=15)
    position_applied = models.CharField("ตำแหน่งที่สมัคร (Position_applied)",max_length=100,
                                        choices=POSITION_CHOICES)
    experience = models.TextField("ประสบการณ์ (Experience)")
    application_status = models.CharField("สถานะใบสมัคร (Status)",max_length=11,
                                          choices=STATUS_CHOICES , default='waiting')

    
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.position_applied}'
    
