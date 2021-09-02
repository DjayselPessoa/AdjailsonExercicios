class Tratamento:

    def tratamento(self, tratarValor, activeRecebido):
        try:
            self.tratarValor = tratarValor
            self.activeRecebido = activeRecebido
            active = self.activeRecebido

            tratandoValor = float
            if self.tratarValor in "Ss":
                active = False
                tratandoValor = 0.0
                return tratandoValor, active

            if self.tratarValor.find(","):
                tratandoValor = float(self.tratarValor.replace(",", "."))
                tratandoValor = round(tratandoValor, 2)
                return tratandoValor, active
            elif self.tratarValor.find("."):
                tratandoValor = float(self.tratando)
                tratandoValor = round(tratandoValor, 2)
                return tratandoValor, active

            if not -999999999.9 <= tratandoValor <= 999999999.9:
                raise ValueError("DADO INCORRETO!")

            else:
                tratandoValor = float(self.tratarValor)
                tratandoValor = round(tratandoValor, 2)
                return self.active, tratandoValor
        except ValueError as e:
            print("LOG: -> ", e)


ObjTratamento = Tratamento()
