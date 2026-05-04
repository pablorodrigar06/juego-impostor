import random
from game.game_config import Difficulty


class WordManager:
    def __init__(self) -> None:
        self._words_by_difficulty: dict[Difficulty, list[str]] = {
            Difficulty.EASY: ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Kylian Mbappé", "Erling Haaland", "Kevin De Bruyne", "Mohamed Salah", "Harry Kane", "Robert Lewandowski", "Karim Benzema",
                "Antoine Griezmann", "Vinícius Jr.", "Rodrygo", "Jude Bellingham", "Luka Modrić", "Toni Kroos", "Pedri", "Gavi", "Frenkie de Jong", "João Félix",
                "Victor Osimhen", "Lautaro Martínez", "Paulo Dybala", "Romelu Lukaku", "Marcus Rashford", "Bukayo Saka", "Phil Foden", "Jack Grealish", "Raheem Sterling", "Mason Mount",
                "Declan Rice", "Bruno Fernandes", "Bernardo Silva", "Rúben Dias", "João Cancelo", "Rodri", "Ilkay Gündogan", "Joshua Kimmich", "Leon Goretzka", "Jamal Musiala",
                "Serge Gnabry", "Leroy Sané", "Kai Havertz", "Florian Wirtz", "Marco Reus", "Thomas Müller", "Achraf Hakimi", "Alphonso Davies", "Trent Alexander-Arnold", "Andrew Robertson",
                "Virgil van Dijk", "Raphaël Varane", "Antonio Rüdiger", "David Alaba", "Kalidou Koulibaly", "Marquinhos", "Thiago Silva", "Éder Militão", "Ronald Araújo", "Jules Koundé",
                "Mike Maignan", "Gianluigi Donnarumma", "Thibaut Courtois", "Jan Oblak", "Alisson Becker", "Ederson", "Yassine Bounou", "Ter Stegen", "Keylor Navas", "Unai Simón",
                "Sadio Mané", "Riyad Mahrez", "Heung-min Son", "Khvicha Kvaratskhelia", "Federico Chiesa", "Nicolo Barella",
                "Christian Eriksen", "Pierre-Emerick Aubameyang", "Olivier Giroud", "James Maddison", "Richarlison", "Gabriel Jesus", "Gabriel Martinelli", "Antony",
                "Lucas Paquetá", "Raphinha", "Fabinho", "Casemiro", "Vitinha", "Rafael Leão", "Theo Hernández"
            ],
            Difficulty.MEDIUM: [ "Lionel Messi", "Cristiano Ronaldo", "Pelé", "Diego Maradona", "Zinedine Zidane", "Johan Cruyff",
                "Franz Beckenbauer", "Paolo Maldini", "Ronaldo Nazário", "Ronaldinho",
                "Michel Platini", "George Best", "Alfredo Di Stéfano", "Ferenc Puskás", "Garrincha", "Lev Yashin",
                "Bobby Charlton", "Eusébio", "Marco van Basten", "Ruud Gullit",
                "Frank Rijkaard", "Lothar Matthäus", "Roberto Baggio", "Romário", "Carlos Valderrama",
                "Hristo Stoichkov", "Davor Šuker", "Dennis Bergkamp", "Eric Cantona", "Alan Shearer",
                "Gabriel Batistuta", "Rivaldo", "Luis Figo", "Raúl González", "Iker Casillas", "Xavi Hernández",
                "Andrés Iniesta", "Sergio Ramos", "Carles Puyol", "Thierry Henry",
                "David Beckham", "Didier Drogba", "Wayne Rooney", "Steven Gerrard", "Frank Lampard", "Paul Scholes",
                "Rio Ferdinand", "John Terry", "Petr Čech", "Gianluigi Buffon",
                "Fabio Cannavaro", "Alessandro Del Piero", "Francesco Totti", "Andrea Pirlo", "Gennaro Gattuso",
                "Clarence Seedorf", "Kaká", "Ronald Koeman", "Patrick Vieira", "Claude Makélélé",
                "Arjen Robben", "Franck Ribéry", "Bastian Schweinsteiger", "Philipp Lahm", "Miroslav Klose",
                "Mesut Özil", "Toni Kroos", "Luka Modrić", "Karim Benzema", "Luis Suárez",
                "Robert Lewandowski", "Zlatan Ibrahimović", "Neymar", "Kylian Mbappé", "Erling Haaland",
                "Kevin De Bruyne", "Mohamed Salah", "Virgil van Dijk", "Manuel Neuer", "Antoine Griezmann",
                "Gareth Bale", "Eden Hazard", "Sadio Mané", "Riyad Mahrez", "Heung-min Son", "Harry Kane",
                "Thomas Müller", "Marco Reus", "Jude Bellingham", "Pedri",
                "Gavi", "Vinícius Jr.", "Rodrygo", "João Félix", "Victor Osimhen", "Lautaro Martínez", "Paulo Dybala",
                "Romelu Lukaku", "Casemiro", "Joshua Kimmich",
                "Frenkie de Jong", "Matthijs de Ligt", "Marcelo", "Dani Alves", "Roberto Carlos", "Ashley Cole", "Cafu",
                "Carlos Alberto Torres", "Daniel Passarella", "Gaetano Scirea",
                "Franco Baresi", "Giuseppe Meazza", "Sandro Mazzola", "Gianni Rivera", "Luigi Riva", "José Santamaría",
                "Hugo Sánchez", "Enzo Francescoli", "Sócrates", "Zico",
                "Falcão", "Jairzinho", "Tostão", "Claudio Caniggia", "Mario Kempes", "Daniel Bertoni", "Uwe Seeler",
                "Karl-Heinz Rummenigge", "Gerd Müller", "Sepp Maier",
                "Oliver Kahn", "Michael Ballack", "Ruud van Nistelrooy", "Edwin van der Sar", "Jaap Stam", "Deco",
                "Pauleta", "Ricardo Carvalho", "Pepe", "Nani",
                "Ángel Di María", "James Rodríguez", "Radamel Falcao", "Edinson Cavani", "Gonzalo Higuaín",
                "Carlos Tevez", "Diego Forlán", "Juan Román Riquelme", "Javier Zanetti", "Esteban Cambiasso"

            ],
            Difficulty.HARD: [ "Lionel Messi", "Cristiano Ronaldo", "Pelé", "Diego Maradona", "Zinedine Zidane", "Johan Cruyff",
                "Franz Beckenbauer", "Paolo Maldini", "Ronaldo Nazário", "Ronaldinho",
                "Michel Platini", "George Best", "Alfredo Di Stéfano", "Ferenc Puskás", "Garrincha", "Lev Yashin",
                "Bobby Charlton", "Eusébio", "Marco van Basten", "Ruud Gullit",
                "Frank Rijkaard", "Lothar Matthäus", "Roberto Baggio", "Romário", "Carlos Valderrama",
                "Hristo Stoichkov", "Davor Šuker", "Dennis Bergkamp", "Eric Cantona", "Alan Shearer",
                "Gabriel Batistuta", "Rivaldo", "Luis Figo", "Raúl González", "Iker Casillas", "Xavi Hernández",
                "Andrés Iniesta", "Sergio Ramos", "Carles Puyol", "Thierry Henry",
                "David Beckham", "Didier Drogba", "Wayne Rooney", "Steven Gerrard", "Frank Lampard", "Paul Scholes",
                "Rio Ferdinand", "John Terry", "Petr Čech", "Gianluigi Buffon",
                "Fabio Cannavaro", "Alessandro Del Piero", "Francesco Totti", "Andrea Pirlo", "Gennaro Gattuso",
                "Clarence Seedorf", "Kaká", "Ronald Koeman", "Patrick Vieira", "Claude Makélélé",
                "Arjen Robben", "Franck Ribéry", "Bastian Schweinsteiger", "Philipp Lahm", "Miroslav Klose",
                "Mesut Özil", "Toni Kroos", "Luka Modrić", "Karim Benzema", "Luis Suárez",
                "Robert Lewandowski", "Zlatan Ibrahimović", "Neymar", "Kylian Mbappé", "Erling Haaland",
                "Kevin De Bruyne", "Mohamed Salah", "Virgil van Dijk", "Manuel Neuer", "Antoine Griezmann",
                "Gareth Bale", "Eden Hazard", "Sadio Mané", "Riyad Mahrez", "Heung-min Son", "Harry Kane",
                "Thomas Müller", "Marco Reus", "Jude Bellingham", "Pedri",
                "Gavi", "Vinícius Jr.", "Rodrygo", "João Félix", "Victor Osimhen", "Lautaro Martínez", "Paulo Dybala",
                "Romelu Lukaku", "Casemiro", "Joshua Kimmich",
                "Frenkie de Jong", "Matthijs de Ligt", "Marcelo", "Dani Alves", "Roberto Carlos", "Ashley Cole", "Cafu",
                "Carlos Alberto Torres", "Daniel Passarella", "Gaetano Scirea",
                "Franco Baresi", "Giuseppe Meazza", "Sandro Mazzola", "Gianni Rivera", "Luigi Riva", "José Santamaría",
                "Hugo Sánchez", "Enzo Francescoli", "Sócrates", "Zico",
                "Falcão", "Jairzinho", "Tostão", "Claudio Caniggia", "Mario Kempes", "Daniel Bertoni", "Uwe Seeler",
                "Karl-Heinz Rummenigge", "Gerd Müller", "Sepp Maier",
                "Oliver Kahn", "Michael Ballack", "Ruud van Nistelrooy", "Edwin van der Sar", "Jaap Stam", "Deco",
                "Pauleta", "Ricardo Carvalho", "Pepe", "Nani",
                "Ángel Di María", "James Rodríguez", "Radamel Falcao", "Edinson Cavani", "Gonzalo Higuaín",
                "Carlos Tevez", "Diego Forlán", "Juan Román Riquelme", "Javier Zanetti", "Esteban Cambiasso", "Lionel Messi", "Cristiano Ronaldo", "Neymar", "Kylian Mbappé", "Erling Haaland", "Kevin De Bruyne", "Mohamed Salah", "Harry Kane", "Robert Lewandowski", "Karim Benzema",
                "Antoine Griezmann", "Vinícius Jr.", "Rodrygo", "Jude Bellingham", "Luka Modrić", "Toni Kroos", "Pedri", "Gavi", "Frenkie de Jong", "João Félix",
                "Victor Osimhen", "Lautaro Martínez", "Paulo Dybala", "Romelu Lukaku", "Marcus Rashford", "Bukayo Saka", "Phil Foden", "Jack Grealish", "Raheem Sterling", "Mason Mount",
                "Declan Rice", "Bruno Fernandes", "Bernardo Silva", "Rúben Dias", "João Cancelo", "Rodri", "Ilkay Gündogan", "Joshua Kimmich", "Leon Goretzka", "Jamal Musiala",
                "Serge Gnabry", "Leroy Sané", "Kai Havertz", "Florian Wirtz", "Marco Reus", "Thomas Müller", "Achraf Hakimi", "Alphonso Davies", "Trent Alexander-Arnold", "Andrew Robertson",
                "Virgil van Dijk", "Raphaël Varane", "Antonio Rüdiger", "David Alaba", "Kalidou Koulibaly", "Marquinhos", "Thiago Silva", "Éder Militão", "Ronald Araújo", "Jules Koundé",
                "Mike Maignan", "Gianluigi Donnarumma", "Thibaut Courtois", "Jan Oblak", "Alisson Becker", "Ederson", "Yassine Bounou", "Ter Stegen", "Keylor Navas", "Unai Simón",
                "Sadio Mané", "Riyad Mahrez", "Heung-min Son", "Khvicha Kvaratskhelia", "Federico Chiesa", "Nicolo Barella", "Sergej Milinković-Savić", "Dušan Vlahović", "Aleksandar Mitrović", "Edin Džeko",
                "Christian Eriksen", "Pierre-Emerick Aubameyang", "Olivier Giroud", "James Maddison", "Jarrod Bowen", "Dominic Calvert-Lewin", "Richarlison", "Gabriel Jesus", "Gabriel Martinelli", "Antony",
                "Lucas Paquetá", "Raphinha", "Douglas Luiz", "Fabinho", "Casemiro", "Fred", "Vitinha", "Gonçalo Ramos", "Rafael Leão", "Theo Hernández"
            ]
        }

    def get_word(self, difficulty: Difficulty) -> str:
        if difficulty not in self._words_by_difficulty:
            raise ValueError(f"Dificultad no válida: {difficulty}")

        return random.choice(self._words_by_difficulty[difficulty])

    def get_word_pair(self, difficulty: Difficulty):
        words = self._words_by_difficulty[difficulty]

        word1 = random.choice(words)
        word2 = random.choice(words)

        while word1 == word2:
            word2 = random.choice(words)

        return word1, word2

    def add_word(self, difficulty: Difficulty, word: str):
        self._words_by_difficulty[difficulty].append(word)