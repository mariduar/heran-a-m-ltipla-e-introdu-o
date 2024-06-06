class document
  def show(self):
      return "Showing document base"

class Printable:
    def print(self):
        return "Print document"

class Editable:
    def edit(self):
        return "Edit document"

class PfDocument(Document,Printable,Editable):
    pass

pdf = PdfDocument()
print(pdf.show()) # Usa metodo de document
print(pdf.print()) # Usa metodo de Printable
print(pdf.edit()) # usa metodo de Editable 
