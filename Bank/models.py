from django.db import models


class forms(models.Model):
    """Автор: Селин Максим
    Таблицы из базы данных, куда кладутся значения из request запросов.
        """
    data = models.CharField(max_length=40, default='None', null=True)


class banks(models.Model):
    """Автор: Селин Максим
    Таблица базы данных, хранит название и регистрационный номер банка
    """
    REGN = models.CharField(max_length=4, default='None', primary_key=True)
    name = models.CharField(max_length=60, default='none')


class banks_d(models.Model):
    """Автор: Селин Максим
        Таблица базы данных, хранит данные из D таблицы DBF"""
    DT = models.CharField(max_length=10, default='None', null=True)
    REGN = models.CharField(max_length=4, default='None', null=True)
    C1 = models.CharField(max_length=15, default='None', null=True)
    C3 = models.CharField(max_length=16, default='None', null=True)


class banks_n(models.Model):
    """Автор: Селин Максим
    Таблица базы данных, хранит данные из N таблицы DBF"""
    DT = models.CharField(max_length=10, default='None', null=True)
    C1 = models.CharField(max_length=15, default='None', null=True)
    C2_1 = models.CharField(max_length=240, default='None', null=True)
    C2_2 = models.CharField(max_length=240, default='None', null=True)
    C2_3 = models.CharField(max_length=240, default='None', null=True)


class banks_s(models.Model):
    """Автор: Селин Максим
    Таблица базы данных, хранит данные из S таблицы DBF"""
    DT = models.CharField(max_length=10, default='None', null=True)
    REGN = models.CharField(max_length=4, default='None', null=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class banks_b(models.Model):
    """Автор: Селин Максим
    Таблица базы данных, хранит данные из B таблицы DBF"""
    REGN = models.CharField(max_length=4, default='None', null=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='None', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)
