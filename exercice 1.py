class Vecteur2D:
    """class vecteur2D."""

    def __init__(self, x0=0, y0=0):
        """Constructeur avec parametres par defaut."""
        self.x = x0  # initialisation de x et y, attributs d'instance
        self.y = y0
        self.nom = "najwa"

    def affiche(self):

        self.nom

    def __str__(self):
        """ Utilisation du print """
        return "x = %d, y = %d" % (self.x, self.y)


# Auto-test ---------------------------------------------------------
if __name__ == '__main__':
    print(" une instance par defaut ".center(50, '-'))
    Vecteur2D()
    # --
    print(" une instance initialisee ".center(50, '-'))
    Vecteur2D(-5.2, 4.1)
    Vecteur2D().affiche()