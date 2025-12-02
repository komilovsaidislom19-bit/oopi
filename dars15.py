# import time
# from functools import wraps
# def vaqt_olchov(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         natija = func(*args,**kwargs)
#         tugadi = time.time()
#         print(f"Funksiya {tugadi-start} soniyada bajarildi.")
#         return natija
#     return wrapper
# @vaqt_olchov
# def hisobla():
#     son=0
#     for i in range(1000):
#         son+=i
#     return son
# print(hisobla())

#dekoratr son qabul qilinishi


#
# def takrorla(n):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             for _ in range(n):
#                 func(*args,**kwargs)
#         return wrapper
#     return decorator
#
# @takrorla(3)
# def salom_ber():
#     print("salom,Diyorbek!")
# salom_ber()




#darsdagi masa salom kapitan deb chiqishi kere
# def takrorla(n):
#     def decorator(func):
#         def wrapper(name,*args,**kwargs):
#             data=func(name,*args,**kwargs)
#             data=f"{data} {n}"
#             return data
#
#         return wrapper
#
#     return decorator
# @takrorla("kapitan")
# def salom_ber(name):
#     return f"salom {name}!"
# print(salom_ber("Diyorbek"))
# print(salom_ber("Odiljon"))
# print(salom_ber("Anashon"))
# print(salom_ber("Abdulaziz"))
# print(salom_ber("Radjabova Amina"))



#