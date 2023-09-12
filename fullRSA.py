import rsa
import time

text = "onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneightteenninteentwentytwentyonetwentytwotwentythreetwentyfourtwentyfivetwentysixtwentyseventwentyeighttwentyninethirtythirtyonethirtytwothirtythreethirtyfourthirtyfivethirtysixthirtyseventhirtyeightthirtyninefourty0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...ONETWOTHREEFOURFIVESIXSEVENEIGHTNINETENELEVENTWELVETHIRTEENFOURTEENFIFTEENSIXTEENSEVENTEENEIGHTTEENNINTEENTWENTYTWENTYONETWENTYTWOTWENTYTHREETWENTYFOURTWENTYFIFETWENTYSIXTWENTYSEVENTWENTYEIGHTTWENTYNINETHIRTYTHIRTYONETHIRTYTWOTHIRTYTHREETHIRTYFOURTHIRTYFIVETHIRTYSIXTHIRTYSEVENTHIRTYEIGHTTHIRTYNINEFOURTY1234567891011121314151611718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneightteenninteentwentytwentyonetwentytwotwentythreetwentyfourtwentyfivetwentysixtwentyseventwentyeighttwentyninethirtythirtyonethirtytwothirtythreethirtyfourthirtyfivethirtysixthirtyseventhirtyeightthirtyninefourty0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...ONETWOTHREEFOURFIVESIXSEVENEIGHTNINETENELEVENTWELVETHIRTEENFOURTEENFIFTEENSIXTEENSEVENTEENEIGHTTEENNINTEENTWENTYTWENTYONETWENTYTWOTWENTYTHREETWENTYFOURTWENTYFIFETWENTYSIXTWENTYSEVENTWENTYEIGHTTWENTYNINETHIRTYTHIRTYONETHIRTYTWOTHIRTYTHREETHIRTYFOURTHIRTYFIVETHIRTYSIXTHIRTYSEVENTHIRTYEIGHTTHIRTYNINEFOURTY1234567891011121314151611718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneightteenninteentwentytwentyonetwentytwotwentythreetwentyfourtwentyfivetwentysixtwentyseventwentyeighttwentyninethirtythirtyonethirtytwothirtythreethirtyfourthirtyfivethirtysixthirtyseventhirtyeightthirtyninefourty0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...ONETWOTHREEFOURFIVESIXSEVENEIGHTNINETENELEVENTWELVETHIRTEENFOURTEENFIFTEENSIXTEENSEVENTEENEIGHTTEENNINTEENTWENTYTWENTYONETWENTYTWOTWENTYTHREETWENTYFOURTWENTYFIFETWENTYSIXTWENTYSEVENTWENTYEIGHTTWENTYNINETHIRTYTHIRTYONETHIRTYTWOTHIRTYTHREETHIRTYFOURTHIRTYFIVETHIRTYSIXTHIRTYSEVENTHIRTYEIGHTTHIRTYNINEFOURTY1234567891011121314151611718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneightteenninteentwentytwentyonetwentytwotwentythreetwentyfourtwentyfivetwentysixtwentyseventwentyeighttwentyninethirtythirtyonethirtytwothirtythreethirtyfourthirtyfivethirtysixthirtyseventhirtyeightthirtyninefourty0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...ONETWOTHREEFOURFIVESIXSEVENEIGHTNINETENELEVENTWELVETHIRTEENFOURTEENFIFTEENSIXTEENSEVENTEENEIGHTTEENNINTEENTWENTYTWENTYONETWENTYTWOTWENTYTHREETWENTYFOURTWENTYFIFETWENTYSIXTWENTYSEVENTWENTYEIGHTTWENTYNINETHIRTYTHIRTYONETHIRTYTWOTHIRTYTHREETHIRTYFOURTHIRTYFIVETHIRTYSIXTHIRTYSEVENTHIRTYEIGHTTHIRTYNINEFOURTY1234567891011121314151611718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneightteenninteentwentytwentyonetwentytwotwentythreetwentyfourtwentyfivetwentysixtwentyseventwentyeighttwentyninethirtythirtyonethirtytwothirtythreethirtyfourthirtyfivethirtysixthirtyseventhirtyeightthirtyninefourty0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...ONETWOTHREEFOURFIVESIXSEVENEIGHTNINETENELEVENTWELVETHIRTEENFOURTEENFIFTEENSIXTEENSEVENTEENEIGHTTEENNINTEENTWENTYTWENTYONETWENTYTWOTWENTYTHREETWENTYFOURTWENTYFIFETWENTYSIXTWENTYSEVENTWENTYEIGHTTWENTYNINETHIRTYTHIRTYONETHIRTYTWOTHIRTYTHREETHIRTYFOURTHIRTYFIVETHIRTYSIXTHIRTYSEVENTHIRTYEIGHTTHIRTYNINEFOURTY1234567891011121314151611718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneightteenninteentwentytwentyonetwentytwotwentythreetwentyfourtwentyfivetwentysixtwentyseventwentyeighttwentyninethirtythirtyonethirtytwothirtythreethirtyfourthirtyfivethirtysixthirtyseventhirtyeightthirtyninefourty0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...ONETWOTHREEFOURFIVESIXSEVENEIGHTNINETENELEVENTWELVETHIRTEENFOURTEENFIFTEENSIXTEENSEVENTEENEIGHTTEENNINTEENTWENTYTWENTYONETWENTYTWOTWENTYTHREETWENTYFOURTWENTYFIFETWENTYSIXTWENTYSEVENTWENTYEIGHTTWENTYNINETHIRTYTHIRTYONETHIRTYTWOTHIRTYTHREETHIRTYFOURTHIRTYFIVETHIRTYSIXTHIRTYSEVENTHIRTYEIGHTTHIRTYNINEFOURTY1234567891011121314151611718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneightteenninteentwentytwentyonetwentytwotwentythreetwentyfourtwentyfivetwentysixtwentyseventwentyeighttwentyninethirtythirtyonethirtytwothirtythreethirtyfourthirtyfivethirtysixthirtyseventhirtyeightthirtyninefourty0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...ONETWOTHREEFOURFIVESIXSEVENEIGHTNINETENELEVENTWELVETHIRTEENFOURTEENFIFTEENSIXTEENSEVENTEENEIGHTTEENNINTEENTWENTYTWENTYONETWENTYTWOTWENTYTHREETWENTYFOURTWENTYFIFETWENTYSIXTWENTYSEVENTWENTYEIGHTTWENTYNINETHIRTYTHIRTYONETHIRTYTWOTHIRTYTHREETHIRTYFOURTHIRTYFIVETHIRTYSIXTHIRTYSEVENTHIRTYEIGHTTHIRTYNINEFOURTY1234567891011121314151611718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneightteenninteentwentytwentyonetwentytwotwentythreetwentyfourtwentyfivetwentysixtwentyseventwentyeighttwentyninethirtythirtyonethirtytwothirtythreethirtyfourthirtyfivethirtysixthirtyseventhirtyeightthirtyninefourty0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...ONETWOTHREEFOURFIVESIXSEVENEIGHTNINETENELEVENTWELVETHIRTEENFOURTEENFIFTEENSIXTEENSEVENTEENEIGHTTEENNINTEENTWENTYTWENTYONETWENTYTWOTWENTYTHREETWENTYFOURTWENTYFIFETWENTYSIXTWENTYSEVENTWENTYEIGHTTWENTYNINETHIRTYTHIRTYONETHIRTYTWOTHIRTYTHREETHIRTYFOURTHIRTYFIVETHIRTYSIXTHIRTYSEVENTHIRTYEIGHTTHIRTYNINEFOURTY1234567891011121314151611718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneightteenninteentwentytwentyonetwentytwotwentythreetwentyfourtwentyfivetwentysixtwentyseventwentyeighttwentyninethirtythirtyonethirtytwothirtythreethirtyfourthirtyfivethirtysixthirtyseventhirtyeightthirtyninefourty0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...ONETWOTHREEFOURFIVESIXSEVENEIGHTNINETENELEVENTWELVETHIRTEENFOURTEENFIFTEENSIXTEENSEVENTEENEIGHTTEENNINTEENTWENTYTWENTYONETWENTYTWOTWENTYTHREETWENTYFOURTWENTYFIFETWENTYSIXTWENTYSEVENTWENTYEIGHTTWENTYNINETHIRTYTHIRTYONETHIRTYTWOTHIRTYTHREETHIRTYFOURTHIRTYFIVETHIRTYSIXTHIRTYSEVENTHIRTYEIGHTTHIRTYNINEFOURTY1234567891011121314151611718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneightteenninteentwentytwentyonetwentytwotwentythreetwentyfourtwentyfivetwentysixtwentyseventwentyeighttwentyninethirtythirtyonethirtytwothirtythreethirtyfourthirtyfivethirtysixthirtyseventhirtyeightthirtyninefourty0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100...ONETWOTHREEFOURFIVESIXSEVENEIGHTNINETENELEVENTWELVETHIRTEENFOURTEENFIFTEENSIXTEENSEVENTEENEIGHTTEENNINTEENTWENTYTWENTYONETWENTYTWOTWENTYTHREETWENTYFOURTWENTYFIFETWENTYSIXTWENTYSEVENTWENTYEIGHTTWENTYNINETHIRTYTHIRTYONETHIRTYTWOTHIRTYTHREETHIRTYFOURTHIRTYFIVETHIRTYSIXTHIRTYSEVENTHIRTYEIGHTTHIRTYNINEFOURTY1234567891011121314151611718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100..."
times = ""
for i in range(100):
    timing = time.time()
    message = text.encode('utf8')
    (pub,priv) = rsa.newkeys(512)
    rsa.encrypt
    timing = time.time()-timing
    times += str(timing) + " "
print(times)