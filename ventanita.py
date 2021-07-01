from tkinter import *

window = Tk()
window.title("Ejemplo de contador")
window.geometry('220x150')

lbl = Label(window, text="0", width=25)  # Etiqueta para mostrar el valor del contador
lbl.grid(column=3, row=2)

# La clase que se ocupa de mantener y mostrar el valor de la cuenta
class Contador:
  def __init__(self, lbl:Label, init=0):
    self.c = init
    self.lbl:Label = lbl

  def next(self):
    self.c = self.c + 1
    self.lbl["text"] = str(self.c)

  def reset(self):
    self.c = 0
    self.lbl["text"] = str(self.c)

# Creamos una instancia del contador, pasándole como parámetro
# la etiqueta donde debe mostrar el resultado
cnt = Contador(lbl)

# Creamos un par de botones, uno para incrementar, otro para reiniciar
btn = Button(window, text="+1", command=cnt.next)
btn.grid(column=2, row=0)
btn = Button(window, text="Reset", command=cnt.reset)
btn.grid(column=3, row=0)

window.mainloop()