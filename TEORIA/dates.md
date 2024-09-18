# Dates

## Tipus disponibles
* datetime.date
    * Atributs year, month, y day.
* datetime.time
    * Atributs hour, minute, second, microsecond i tzinfo.
* datetime.datetime
    * Atributs year, month, day, hour, minute, second, microsecond i tzinfo.
* datetime.timedelta
    *  Atributs date, time o datetime a una resolución de microsegundos.

## timedelta
```python
class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
```

Només s'emmagatzemen days, seconds i microseconds. Els milisegons es transformen a microsegons, els minuts a segons, les hores a segons i les setmanes a dies.

Podem operar amb +, -, *, //, % ...

Un objecte timedelta es vertader si no es igual a timedelta(0).

### Mètodes
* timedelta.total_seconds()
Retorna el nombre de segons. Equival a td / timedelta(seconds=1).

Per a unitats que no siguen segons hem de fer la divisió directamente. Per exemple:

    td / timedelta(microseconds=1)

## date
```python
class datetime.date(year, month, day)
classmethod date.today()
```
### Mètodes
* date.replace(year=self.year, month=self.month, day=self.day)
```python
d = date(2002, 12, 31)
d.replace(day=26)
datetime.date(2002, 12, 26)
```

* date.weekday(): Retorna el dia de la setmana, dilluns és 0 y el diumenge és 6.
* date.isoweekday(): Retorna el dia de la setmana, dilluns és 1 y el diumenge és 7.
* date.strftime(format): Retorna una cadena amb un format determinat.

Alguns codis de format (dos dígits):
%S (segons), %M (minuts), %m (mes), %y(any), %Y (any 4 dígits), %H (hora 24 hores).

## datetime
```python
class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

classmethod datetime.now(tz=None)   # data i hora d'ara

classmethod datetime.combine(date, time, tzinfo=self.tzinfo)    # Crea un datetime a partir d'un date i un time

classmethod datetime.strptime(cadena, format)  # Crea un datetime a partir de la cadena que li passen, la qual té el format especificat.
# Llança ValueError si le format de la cadena no casa amb l'especificat.
```

### Atributs
* datetime.year
* datetime.month
* datetime.day
* datetime.hour
* datetime.minute
* datetime.second
* datetime.microsecond

# Mètodes
* datetime.date()
* datetime.time()
* datetime.replace(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)
* datetime.weekday(): Dia de la setmana on 0 és dilluns i 6 és diumenge.
* datetime.isoweekday(): Dia de la setmana on 1 és dilluns i 7 és diumenge.
* datetime.strftime(format): Retorna una cadena amb el format especificat.

## time
```python
class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
```

### atributs
* time.hour
* time.minute
* time.second
* time.microsecond

### mètodes
* time.replace(hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)
* time.strftime(format): Retorna una cadena amb el format especificat.




