from typing import Optional
class Singleton:
    single: Optional["Singleton"] = None

    def new(cls, *args, **kwargs):  
        if not cls.single:
            cls.single = super().new(cls)

        return cls.single