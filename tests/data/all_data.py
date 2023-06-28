from datetime import datetime

"""
채점을 위한 파일입니다. 수정하지 마세요.
"""
ALL_VISIT_LOG = [
            (None, datetime.strptime('2022-07-11 12:30:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-11 14:45:00', '%Y-%m-%d %H:%M:%S'), 'meeting'),
            (None, datetime.strptime('2022-07-12 15:20:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-12 16:50:00', '%Y-%m-%d %H:%M:%S'), 'visit family'),
            ('A00001', datetime.strptime('2022-07-11 11:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-11 18:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('A00001', datetime.strptime('2022-07-12 08:15:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-12 17:56:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('A00001', datetime.strptime('2022-07-13 09:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-13 18:20:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('A00001', datetime.strptime('2022-07-14 08:30:00', '%Y-%m-%d %H:%M:%S'), None, 'work'),
            ('A08771', datetime.strptime('2022-07-11 09:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-11 17:56:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('A08771', datetime.strptime('2022-07-12 09:20:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-12 18:20:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('A08771', datetime.strptime('2022-07-13 09:20:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-13 18:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('A08771', datetime.strptime('2022-07-14 08:30:00', '%Y-%m-%d %H:%M:%S'), None, 'work'),
            ('B00100', datetime.strptime('2022-07-11 10:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-11 19:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('B00100', datetime.strptime('2022-07-12 08:30:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-12 19:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('B00100', datetime.strptime('2022-07-13 08:30:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-13 18:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('B00100', datetime.strptime('2022-07-14 08:30:00', '%Y-%m-%d %H:%M:%S'), None, 'work'),
            ('C00001', datetime.strptime('2022-07-11 09:20:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-11 18:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00001', datetime.strptime('2022-07-12 10:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-12 18:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00001', datetime.strptime('2022-07-13 09:20:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-13 18:20:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00002', datetime.strptime('2022-07-11 09:30:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-11 18:20:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00002', datetime.strptime('2022-07-12 09:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-12 17:56:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00002', datetime.strptime('2022-07-13 08:15:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-13 17:56:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00129', datetime.strptime('2022-07-11 09:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-11 18:20:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00129', datetime.strptime('2022-07-12 10:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-12 18:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00129', datetime.strptime('2022-07-13 10:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-13 18:00:00', '%Y-%m-%d %H:%M:%S'), 'work')
        ]

ALL_EMPLOYEE = [
            ("A00001", "Male", "Moon", "10-199, Gang-nam, Seoul", 1, "C00001", 30, "Senior engineer"),
            ("A08771", "Others", "Peach", "203-3, Guro, Seoul", 1, "C00001", 26, "Junior engineer"),
            ("B00100", "Female", "Sun", "587/8, Gwan-ak, Seoul", 2, "B00102", 25, "Associate marketer"),
            ("B00102", "Female", "Ran", "290-10, Gwanghwamun, Seoul", 2, "C00000", 45, "Director"),
            ("C00000", "Male", "K", "1010, Sung-soo, Seoul", None, None, 51, "CEO"),
            ("C00001", "Male", "Lion", "53-3, Namyang-ju, Gyonghi", 1, "C00000", 55, "CTO"),
            ("C00002", "Others", "Cindy", "100, Jong-ro, Seoul", 3, "C00000", 52, "Director"),
            ("C00129", "Male", "Alex", "20-331, Bundang, Gyonggi", 3, "C00002", 40, "Director")
        ]