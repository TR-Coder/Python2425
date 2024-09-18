# Kivy
https://github.com/YingLiu4203/LearningKivy

## Introducció
Una interfície d’usuari està formada per widgets. Tenim:
* Widgets visibles
* Layout widgets (widgets de composició) que actuen com a widgets contenidors i permeten definir les dimensions i el posicionament dels widgets que agrupen.

Els widgets es poden crear utilitzant codi Python o millor, utilitzant kvlang per la seua senzillesa i sintaxi clar.

En codi, un widget és una subclasse de la classe kivy.uix.widget.Widget

Els widgets tenen propietats (id, color, text, font size) i poden disparar esdeveniments (touch down, touch move, and touch up...)


## Arbre de widgets
Els widgets s’organitzen és una estructura jeràrquica en forma d’arbre. El widget arrel s’anomena root. Dins d’un arxiu .kv el widget arrel dins d’una arxiu .kv s’identifica per ser el widgets de més a l’esquerra. La relació pare-fill s’expressa utilitzant identació.

En el següent exemple _GridLayout_ és un layout widget que conté dos widgets Label com a fills i, a més, és el root widget. 
```python
GridLayout:
    Label:
        text: "Hello World"
    Label:
        text: "Best Regards"
```

## Posició i demensió dels widgets
La major part dels widgets tenen una dimensió (size) i un posicionament (position) per defecte.
En una finestra d'escriptori, el widget arrel es posiciona en la part superior esquerra de la pantalla i ocupa tot l'espai disponible de la pantalla.
Un widget botó té, per defecte, unes dimensions de 100px d'ample (width) i 100px d'alçària (height) i se situa en la part inferior esquerra del seu pare.

Els càlculs de les dimensions y del posicioment dels widgets depenen tant del widget pare com de tots els seus fills. Un wiget fill pot especificar la seua dimensió i el posiciomanent al seu pare, però és este qui té una visió general i qui acabarà determinant les dimensions i el posicionament dels seus fills. En ocasions les regles que aplica el pare ignoren les preferències dels fills.

Kivy utilitza un parell de coordenades (x, y) per a especificar la posició d'un widget al seu pare. x és el valor horitzontal on 0 significa el costat esquerre. De la mateixa manera, y és el valor vertical on 0 significa la part inferior.

```python
Widget:
    Button:
        pos: 100, 100
        size: 150, 150
    Button:
        x: 100
        y: 300
        width: 150
        height: 150
```

## Organització amb Layouts
En la següent pàgina es descriuen els layouts: https://kivy.org/doc/stable/guide/widgets.html#organize-with-layouts

El Layout més emprat és _BoxLayout_: Els fills es disposen l'un al costat de l'altre en sentit vertical o horitzontal. En la disposició vertical, tots els fills tenen la mateixa amplada que el BoxLayout. En l'horitzontal, tenen la mateixa alçada que el BoxLayout.

```python
BoxLayout:
    orientation: 'vertical'
    padding: 10
    BoxLayout:
        Button:
            text: "First Row, First Column"
            bold: True
        Button:
            text: "First Row, Second Column"
            color: [1, 0, 0, 1]
            bold: True
    BoxLayout:
        Button:
            text: "Second Row, First Column"
            color: [0, 1, 0, 1]
            bold: True
        Button:
            text: "Second Row, Second Column"
            color: [0, 0, 1, 1]
            bold: True
```

En l'exemple anterior, a més de la propietat orientation, la propietat _padding_ indica el paddind entre la caixa del Layout i els seus fills interiors, i la propietat spacing indica l'espai entre els fills.

## Dimensions (widget size)
Kivy té dos tipus de dimensions: Absolutes (absolute size) i relatives (hint size).

### Dimensions absolutes (absolute size)
És un nombre (int o float), per defecte 0, amb unes unitats, per defecte px.
En Kivy els widgets tenen unes dimensions per defecte de (100px, 100px).

Un píxel, px, en la unitat mínima de visualització d'una pantalla. La dimensió física d'un píxel varia segons la resolució de la pantalla. Un píxel en una pantalla de baixa resolució és major que un píxel en una pantalla d'alta resolució de les mateixes dimensions.

A banda del píxels, tenim mm, cm, in, dp i sp.
Una línia d'un cm és el mateix centímetre en un pantalla que sobre un paper.

* __dp__ (density-independent pixels o display pixel). Una polzada és aproximadament igual a 72 dp. És una mida independent de la resolució. Es recomana utilitzar dp per especificar la mida del widget.
* __sp__ (scale-independent pixels). És com la unitat dp, però s'escala amb la mida de la lletra. Es recomana utilitzar sp com a unitat de mida de lletra.

En general, hi ha dues recomanacions senzilles d'unitats mètriques:
* _dp_ per a _width_ i _height_
* _sp_ per a _font-size_

### Dimensions relatives (hint size)
Les dimensions relatives tenen un valor (int o float) però no tenen unitats.

Un widget té 3 propietats de mida relativa:
* size_hint_x: width relativa.
* size_hint_y: height relativa.
* size_hint: una combinació de les anteriors (size_hint_x, size_hint_y).

Per defecte, tots els widgets d'un layout tenen una dimensió relativa d'1 i això vol dir que tots els widgets en un layout tenen la mateixa amplada i la mateixa alçada. Una dimensió relativa només és significativa en comparació amb altres valors relatius dins del mateix layout pare. Per exemple:

```python
BoxLayout:
    orientation: 'vertical'
    padding: "10dp"
    BoxLayout:
        size_hint_y: 200
        Button:
            size_hint_x: 2
        Button:
            size_hint_x: 6
    BoxLayout:
        size_hint_y: 600
        Button:
            size_hint_x: 2
        Button:
            size_hint_x: 0.5
```

En el codi anterior, l'alçària dels botons en al primera fila són 1/3 de l'alçària dels botons de la segona fila ja que el ratio és 200:600.
D'igual manera, en la segona fila, el primer botó és 4 vegades més ample que el segon ja que le ratio és 2:0.5

### Dimensió controlada (orientació)
La dimensió controlada és la orientació de la caixa en un layout, per defecte és _horizontal_.

En un layout, la mida dels fills en la dimensió controlada és la seua mida relativa dividida per la suma relativa de tots els fills. Seguint amb l'exemple anterior: l'horientació del BoxLayout exterior és vertical, així l'alçària relativa del primer fill és 200 / (200 + 600), un 25% de l'alçària total. D'igual manera, en el segon fill és 600 / (200 + 600), un 75%. Per altra banda, el fills dels BoxLayout interiors tenen orientatzió horitzontal. En el primer fill, els botons ocupen un 25% i un 75% d'amplària. En el segon fill, els botons ocupen un 80% i 20%.

Un dimensió no controlada es dona quan hi ha un sol widget en esta dimensió. Per defecte, la dimensió relativa és 1 en la dimensión no controlada i pren tot l'espai en esta dimensió. Una dimensió relativa menor a 1 en la dimensió no controlada reduïx la mida en esta dimensió. Un valor major a 1 és ignorat.

En el següent codi, la dimensió controlada és vertical, per tant l'alçaria relativa del botó és 0.5/0.5=1, el 100% de l'alçària del BoxLayout. En la dimensió no controlada, l'horitzontal, és la indicada en size_hint_x: 0.5, o siga el 50% del pare, del BoxLayout.

```python
BoxLayout:
    orientation: 'vertical'
    Button:
        size_hint_x: 0.5
        size_hint_y: 0.5
```

### Dimensions absolutes
Quan utilitzem una mida absoluta per a un widget fill en un layout, hem d'establir explícitament la mida relativa corresponent a None. En cas contrari, Kivy utilitzarà la mida relativa predeterminada d'1.

En el següent codi, les propietats height i width no funcionen si no afegim els corresponents None a la mida relativa corresponent.

```python
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        height: "200dp"
        size_hint_y: None   # Hem d'afegir-lo
        Button:
            size_hint_x: 2
        Button:
            size_hint_x: 6
    BoxLayout:
        height: "200dp"
        size_hint_y: None   # Hem d'afegir-lo
        width: "200dp"
        size_hint_x: None   # Hem d'afegir-lo
        Button:
            size_hint_x: 2
        Button:
            size_hint_x: 0.5
```

## Esdeveniments
### Aplicacions conduïdes per esdeveniments
La majoria d'aplicacions GUI són aplicacions conduïdes per esdeveniments. La aplicació entra en un bucle principal esperant que passen diferents esdeveniments. En kivy a cada iteració del bucle principal s'anomena _time frame_.
Quan es produïx un esdeveniment este és gestionat per una funció manejadora o callback. Les funcions callback es registren de manera que el _event dispatcher_ (manejador d'esdeveniments) sap els esdeveniments en què l'aplicació està interessats. El procés d'enregistrament vincula (bind) una callback a un esdeveniment. 

https://kivy.org/doc/stable/guide/events.html

### Planificació d'esdeveniments
Un esdeveniment molt comú definit per l'usuari és un esdevenimentde rellotge. Per exemple, clock.schedule_interval(my_callback, 1/30.0) programa un esdeveniment que s'activa 30 vegades per segon. Quan l'esdeveniment es dispara es crida la funció my_callback.

### La classe Property
#### Introducció
Un tipus especial de fonts d'esdeveniments és una propietat de widget. 

Un widget sol tindre moltes propietats com ara la seva posició, mida o text. En molts casos volem ser notificats quan estos valors canvien. Per exemple, quan un widget canvia la seva posició a una zona especial, volem canviar-ne el color. Com açò és molt comú en una aplicació GUI, Kivy definex una classe Property que implementa el patró d'observador. De manera semblant a un esdeveniment, una instància de Property manté una llista d'observadors.Normalment un observador és una funció callback. Quan el valor d'una instància Property canvia, crida els seus observadors amb dos paràmetres: la instància del widget Property i el valor modificat.

Una propietat d'un widget és una instància de la classe Property. No és la classe integrada en Python property que s'utilitza amb el decorador @property. La classe Property és un descriptor de Python que implementa el patró observador i altres característiques especials com ara la validació de valors.

La classe Property té els següents mètodes relacionats amb els esdeveniments:
* bind(): enllaça un esdeveniment de property a un o més manejadors, és a dir, enllaça un observer a un esdeveniment de canvi de valor.
* unbind(): desenllaça un manejador.
* dispatch(): dispara un esdeveniment manualment. En general, Kivy dispara esdeveniments automàticament quan passa alguna cosa. Però podem disparar un esdeveniment mitjançant este mètode.

#### Les classes Property
La classe Property és la classe pare per a una sèrie de tipus de propietat específics. Property no s'ha d'instanciar directament. A continuació es mostren algunes classes de propietats comunes que es poden utilitzar per representar valors específics del tipus, valors vàlids i dispara d'esdeveniments quan els seus valors canvien.

* NumericProperty: representa un valor int o float i un tipus. El valor per defecte és 0 amb un tipus px. Un valor NumericProperty es pot inicialitzar amb un nombre i un tipus numèrics. Per exemple, 0.5, '5dp' i (7.5, 'sp') són tots valors vàlids.
* BoundedNumericProperty: representa un valor numèric que té un límit mínim i/o màxim.
* StringProperty: representa un valor de cadena. El valor per defecte és una cadena buida ''.
* ListProperty: representa una llista. Per defecte és una llista buida.
* ObjectProperty: representa un objecte Python. Primer és un esdeveniment quan s'assigna a un objecte Python diferent.
* BooleanProperty: representa un valor booleà.
* OptionProperty: representa una cadena que ha de ser d'una llista predefinida de cadenes.
* ReferenceListProperty: representa una tupla d'altres propietats. La propietat pos d'un widget és una instància de ReferenceListProperty. Quan es llig la propietat, retorna una tupla de valors de Python.
* DictProperty: representa un diccionari.

#### Esdeveniments Property
L'ús d'esdeveniments de propietat implica quatre passos: declarar una propietat, vincular un esdeveniment de canvi de propietat, canviar el valor d'una propietat i manejar un esdeveniment de propietat.

* Declarar un propietat
En Kivy, una propietat s'ha de declarar com un atribut de classe i no com un atribut d'instància. Un propietat és una instància d'una de les classes property del punt anterior.
En el següent exemple tenim una classe de Widget amb 2 propietats.
```python
class CustomBtn(Widget):
    pressed = ListProperty([0, 0])
    demo_prop = NumericProperty(0)
```

* Vincular un esdeveniment de canvi de propietat
Hi ha dos maneres per a vincular un esdeveniment de canvi de propietat.

    * Dins d'un widget definir un mètode d'instància amb el nom on_property_name.

```python
def on_pressed(self, instance, pos):
    print 'pressed at {pos}'.format(pos=pos)

def on_demo_prop(self, instance, value):
    print 'on_demo_prop value changed to {}'.format(value)
```

    * Fora del widget, utilitzar el mètode bind()
```python
cb.bind(pressed=self.btn_pressed)
cb.bind(demo_prop=self.demo_changed)
```

* Canviar el valor d'una propietat
En el següent codi quan es dispara un esdeveniment touch_event es llança el manejador on_touch_down que canviarà el valor de la propietat pressed.
```python
def on_touch_down(self, touch):
    if self.collide_point(*touch.pos):
        self.pressed = touch.pos
        return True
    return super(CustomBtn, self).on_touch_down(touch)
```

* Manejar un esdeveniment Property
Tots els manejadors d'un esdeveniment de canvi de propietat es criden quan canvia el valor de la propietat.

#### El dispatcher d'esdeveniments
Tots les classes widget de Kivy són subclasses de la classe EventDispatcher. Esta classe té els següents mètodes relacionats amb esdeveniments:

* bind(): vincula un esdeveniment definit per un widget a un més manejadors.
* unbind(): desvincula un o més manejadors.
* register_event_type(): registra un tipus d'esdeveniment.
* dispatch(): Dispara un esdeveniment. Normalment kivi dispara els esdeveniments automàticament quan passa alguna cos. Però també els podem llançar nosaltres.
* events(): retorna tots els esdeveniment en la classe.
* get_property_observers(): retorna una llista del manejadors vinculats a un esdeveniment.

Per a implementar un dispatcher d'esdeveniment seguirem dos passos:
* Registrar un tipus d'esdeveniment. El seu nom ha de començar amb el prefix on_.  Utilitzarem el mètode register_event_type().
* Crear un mètode manejador per defecte amb el mateix nom del tipus d'esdeveniment. El manejador es crida quan es dispara un esdeveniment del tipus d'esdeveniment.

Per a llançar un esdeveniment Dispatcher usem el mètode dispatch(). Per utilitzar un esdeveniment, viculem una callback al tipus d'esdeveniment. La vinculació la poden fer utilitzant el mètode bind() o amb un mètode on_event_type() on el nom seguix la convenció on_ i event_type.

Per exemple:
```python
class MyEventDispatcher(EventDispatcher):
    def __init__(self, **kwargs):
        self.register_event_type('on_test')                     # Registrem un tipus d'esdeveniment anomenat on_test.
        super(MyEventDispatcher, self).__init__(**kwargs)

    def on_test(self, *args):                                   # Mètode 1: Manejador del tipus d'esdeviment on_test. Tenen el mateix nom.
                                                                # Estem dins de la classe MyEventDispatcher.
        pass


def my_callback(value, *args):                                  # Mètode 2: Manejador del tipus d'esdeviment on_test.
    print "Hello, I got an event!", args                        # Estem fora de la classe MyEventDispatcher.


class HelloWorldApp(App):
    pass

if __name__ == '__main__':

    ev = MyEventDispatcher()
    ev.bind(on_test=my_callback)                                # Mètode 2: Vinculem un dispatcher amb el seu manejador utilitzant bind() 

    ev.dispatch('on_test', 'test_message')

    HelloWorldApp().run()
```

#### Esdeveniments de Widget
Un widget és una subclasse de EventDispatcher, per tant pot vincular esdevenimets Dispatcher, esdeveniments propis del widget i també esdeveniments Property.

#### Bombeig d'esdeveniments
Els esdeveniments es reben en l'ordre invers en què els widgets s'afegeixen al widget arrel. Exemple:



https://ryan-ashton.medium.com/pythons-kivy-self-root-app-76e20962e8a



# kivi
El que veem per pantalla és una composició de widgets estructura en forma d’un arbre de widgets.

Este arbre el podem crear per codi Python directament o millor utilitzant un llenguatge específic, kv. El llenguatge kv permet crear la UI d’una manera declarativa, o siga dir què ha de mostrar l’UI però sense dir com es fa. En definitiva, estem separant la lògica de l’aplicació de la seua UI.

Com a exemple, el següent codi mostra com codificar una jerarquia de widget amb Python i com s’expressaria esta mateixa jerarquia amb kv.

```python
root = MyRootWidget()
box = BoxLayout()
b1 = Button()
b2 = Button()
box.addwidget(b1)
box.addwidget(b2)
root.addwidget(box)
```

```python
MyRootWidget:
    BoxLayout:
         Button:
         Button:
```

En el nostre primer programa l’estructura de widget està formada només per una Label(). En esta exemple no utilitzarem kv.
Observem que:
* La classe principal (HolaMonApp) hereta d'App.
* La classe principal sobreescriu el mètode build i retorna una instància de la classe Widget o algun derivat seu, en el nostre cas, Label.

```python
import kivy
from kivy.app import App
from kivy.uix.label import Label

class HolaMonApp(App):
    def build(self):
        return Label(text='Hola')

HolaMonApp().run()
```

Ara implementarem el mateix codi utilitzant kv.
```python
import kivy
from kivy.app import App
from kivy.uix.label import Label

class HolaMonApp(App):
    def build(self):
        return Label()     # Hem llevat el contingut anterior de text='hola'.

HolaMonApp().run()
```

En la part de kv, declarem l'UI corresponen a alguna classe __ja declarada previament__ en l'aplicació de Python. En este cas, la classe _Label_, que el programa Phyton la tenim declarada per a ver fet un _import Label_.
Fixem-nos també que _Label_ està entre parèntesis _<>_. Això indica que estem modificant la classe _Label_ i que tota instància de Label vorà els mateixo canvis. Nosaltres la instànciem quan fem _return Label()_. 
```python
#:kivy 1.0.9
<Label>:
    text: 'Hola mon'
```

En general, modificar una classe base com Label no és bona idea ja que afectarà a totes les instàncies de Label que creem posteriorment.
En el següent programa, crearem un widget personalitzat anomenat CustomWidget. Este deriva de Widget que és la classe base de tots els Widgets.
Fixem-nos que la classe CustomWidget no té cap implementació, només l'estem declarant. En la part de kv, implementarem la part gràfica.

```python
import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class CustomWidget(Widget):         # Delaració
    pass

class HolaMonApp(App):
    def build(self):
        return CustomWidget()       # Instanciació

HolaMonApp().run()
```

```python
#:kivy 1.0.9
<CustomWidget>:                     # Implementació UI
    TextInput:
        hint_text: 'Caixa de text'
        pos: 20, 150
        size: 300, 40
    Button:
        text: 'Primer'
        pos: 20, 20
        size: 120, 40
        color: .7, .6, .4, .1
    Button:
        text: 'Segon'
        pos: 200, 20
        size: 120, 40
        color: .7, .6, .4, .1
```

Fixem-no que _TextInput_ i _Button_ no van entre <>. Això significa que estem creant una __instància__ de _TextInput_ i dos instàncies de _Button_.

En el codi anterior estem repetint codi en les propietats _size_ i _color_ de la classe _Button_. Ho podem millorar de la següent manera:

```python
#:kivy 1.0.9
<CustomButton@Button>:
    size: 120, 40
    color: .7, .6, .4, .1

<CustomWidget>:
    TextInput:
        hint_text: 'Caixa de text'
        pos: 20, 150
        size: 300, 40
    CustomButton:
        text: 'Primer'
        pos: 20, 20
    CustomButton:
        text: 'Segon'
        pos: 200, 20
```
En el codi anterior obsevem la declaració de _<CustomButton@Button>:_
Com que en el codi de Phyton no hem declarat que la classe CustomButton deriva de Button, ho hem de fer ací indicant-lo amb @Button.

En el següent codi, declararem en Python que CustomButton és un Button i això ens permetrà llevar el @Button del kv.
```python
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class CustomButton(Button):     # Declarem que CustomButton deriva de Button
    pass

class CustomWidget(Widget):
    pass

class HolaMonApp(App):
    def build(self):
        return CustomWidget()

HolaMonApp().run()
```

```python
#:kivy 1.0.9
<CustomButton>:                 # Simplifiquem llevant el @Button
    size: 120, 40
    color: .7, .6, .4, .1

<CustomWidget>:
    TextInput:
        hint_text: 'Caixa de text'
        pos: 20, 150
        size: 300, 40
    CustomButton:
        text: 'Primer'
        pos: 20, 20
    CustomButton:
        text: 'Segon'
        pos: 200, 20
```

Per defecte, les propietats (de widget) _pos_ i _size_ treballen amb píxels com a unitat de mesura.

De moment, no hem utilitat encara cap layout per a posicionar els widgets per la qual cosa el posicionament es fa de manera absoluta. Això fa que que la posició dels widgets siguen sempre la mateixa, independement de les dimensions de la finestra.

En el següent codi anem a posicionar el TextInput i els dos CustomButom de manera relativa al marc de la finestra. No utilitzarem cap layout, que seria el millor, sinó que farem nosaltres els càlculs. Aprofitarem el codi de Python i modificarem només el kv.

```python
#:kivy 1.0.9
<CustomButton>:
    size: 120, 40
    color: .7, .6, .4, .1

<CustomWidget>:
    TextInput:
        hint_text: 'Caixa de text'
        pos: root.x + 20, root.top - self.height - 20
        size: 300, 40
    CustomButton:
        text: 'Primer'
        pos: root.x + 20, root.y + 20
    CustomButton:
        text: 'Segon'
        pos: root.right - self.witdh - 20, root.y + 20
```

Fixem-nos amb l´ús de __root__ i __self__.

* _self_ fa referència al propi widget en què estem, TextInput o CustomButton.
* _root_ és el widget arrel del qual pengen la resta de widgets, en el nostre cas és CustomWidget.

És important saber que el punt (0,0) de referència se situa en la part inferior esquerra. Això diferix de la majoria frameworks on sol situar-se en la part superior esquerra.

## Layouts
Un Layout és una subclasse de Widget que implementa diferents estratègies per a organitzar els widgets que conté.
Els layout permeten utilitzar coordenades proporcionals que evitaran que hagem de fer càlculs com en l'exemple anterior.

En este exemple farem servir un FloatLayout.

```python
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class FloatLayoutApp(App):
    def build(self):
        return FloatLayout()

FloatLayoutApp().run()
```

```python
<Button>:
  color: .8,.9,0,1
  font_size: 32
  size_hint: .4, .3

<FloatLayout>:
  Button:
    text: 'Hello'
    pos_hint: {'x': 0, 'top': 1}
  Button:
    text: 'World!'
    pos_hint: {'right': 1, 'y': 0}
```

En el codi kv treballam a posicionament (pos_hint) i dimensions proporcionals (size_hint). Els valors varien entre 0 i 1, que corresponen d'un 0 a un 100%.

Així, el __size_hint: .4, .3__ escala l'amplada del botó a un 40% i escala l'alçada un 30%, respecte el FloatLayout. Realment, size_hint és un ReferenceListProperty de les propietats (size_hint_x, size_hint_y) on, size_hint_x i size_hint_y són unes NumericProperty que per defecte valen 1.

Per altra banda, __pos_hint__ és un diccionari, realment un ObjectProperty que conté un diccionari, que permet també permet posicionar un widget dins del layout on està situat.

En este diccionari:
* Les claus __x__, __right__ i __center__ són respecte l'eix x. Les podem entendre com:
    * x és la vora esquerra del widget
    * right és la vora dreta
* Les claus __y__, __top__ i __center_y__ són respecte l'eix y. Les podem entendre com:
    * y és la vora inferior del widget
    * top és la vora superior

__Exemples:__

https://prosperocoder.com/posts/kivy/kivy-part-10-widget-size-position-in-layouts/

El codi python serà:
```python
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class HolaMonApp(App):
    def build(self):
        return FloatLayout()
HolaMonApp().run()
```


```python
#:kivy 1.0.9
<CustomButton@Button>:
    size_hint: .2, .1           # El botó té un ample del .2 del FloatLayout

<FloatLayout>:
    CustomButton:
        text: 'Botó 1'
        pos_hint: {'x': 0}      # vora esquerra del botó en x=0
    CustomButton:
        text: 'Botó 2'
        pos_hint: {'x': .5}     # vora esquerra del botó en x=0.5
    CustomButton:
        text: 'Botó 3'
        pos_hint: {'x': 1}      # vora esquerra del botó en x=1
```
![Error ruta](kivy_img/imatge_001.png)


```python
#:kivy 1.0.9
<CustomButton@Button>:
    size_hint: .2, .1               # El botó té un ample del .2 del FloatLayout

<FloatLayout>:
    CustomButton:
        text: 'Botó 1'
        pos_hint: {'x': -2}         # El botó està forà de la finestra per l'esquerra  
    CustomButton:
        text: 'Botó 2'
        pos_hint: {'x': -.1}        # El botó té un ample de .2 i la vora esquerra està en x=0.1
    CustomButton:
        text: 'Botó 3'
        pos_hint: {'x': .9}         # El botó té un ample de .2 i la vora esquerra està en x=0.9
```
![Error ruta](kivy_img/imatge_002.png)

```python
#:kivy 1.0.9
<CustomButton@Button>:
    size_hint: .2, .1                   # El botó té un ample del .2 del FloatLayout

<FloatLayout>:
    CustomButton:
        text: 'Botó 1'
        pos_hint: {'x': 0}              # vora esquerra del botó en x=0
    CustomButton:
        text: 'Botó 2'
        pos_hint: {'center_x': .5}      # centre horitzontal del botó en x=.5
    CustomButton:
        text: 'Botó 3'
        pos_hint: {'right': 1}          # vora detra del botó en x=1
```
![Error ruta](kivy_img/imatge_003.png)

```python
#:kivy 1.0.9
<CustomButton@Button>:                  # El botó té un ample del .2 del FloatLayout
    size_hint: .2, .1

<FloatLayout>:
    CustomButton:
        text: 'Botó 1'
        pos_hint: {'right': .1}         # vora dreta del botó en x=.1
    CustomButton:
        text: 'Botó 2'
        pos_hint: {'right': .5}         # vora dreta del botó en x=.5
    CustomButton:
        text: 'Botó 3'
        pos_hint: {'center_x': .75}     # centre horitzontal del botó en x=.75
```
![Error ruta](kivy_img/imatge_004.png)

```python
#:kivy 1.0.9
<CustomButton@Button>:  
    size_hint: .2, .1                   # El botó té un ample del .2 del FloatLayout

<FloatLayout>:
    CustomButton:
        text: 'Botó 1'
        pos_hint: {'x': .1, 'top': .5}              # vora dreta del botó a x=.1, vora superior a y=.5
    CustomButton:
        text: 'Botó 2'
        pos_hint: {'center_x': .5, 'center_y': .5}  # centre horitzontal del botó a x=.5, centre vertical del botó a x=.5
    CustomButton:
        text: 'Botó 3'
        pos_hint: {'right': 1, 'y': .2}             # vora detra del botó a x=1, vora inferior del botó a y=.2
```
![Error ruta](kivy_img/imatge_005.png)






