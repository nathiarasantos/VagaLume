from abc import ABC, abstractmethod
from modelos.interfaces import Baixavel, Avaliavel


class Midia(ABC):
    def __init__(self, titulo, ano_lancamento):
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento

    @abstractmethod
    def reproduzir(self):
        pass

    @abstractmethod
    def tempo_total(self):
        pass

    def __str__(self):
        return f"{self.titulo} ({self.ano_lancamento})"


class Video(Midia):
    def __init__(self, titulo, ano_lancamento, resolucao):
        super().__init__(titulo, ano_lancamento)
        self.resolucao = resolucao


class Audio(Midia):
    def __init__(self, titulo, ano_lancamento, autor):
        super().__init__(titulo, ano_lancamento)
        self.autor = autor


class Filme(Video, Baixavel, Avaliavel):
    def __init__(self, titulo, ano_lancamento, resolucao, duracao_minutos):
        super().__init__(titulo, ano_lancamento, resolucao)
        self.duracao_minutos = duracao_minutos
        self.avaliacoes = []

    def reproduzir(self):
        return f"Reproduzindo filme '{self.titulo}' em {self.resolucao}."

    def tempo_total(self):
        return self.duracao_minutos

    def baixar(self):
        return f"Download do filme '{self.titulo}' concluído."

    def remover_download(self):
        return f"Download do filme '{self.titulo}' removido."

    def avaliar(self, nota):
        self.avaliacoes.append(nota)
        return f"Filme '{self.titulo}' avaliado com nota {nota}."

    def media_avaliacoes(self):
        if not self.avaliacoes:
            return 0.0
        return sum(self.avaliacoes) / len(self.avaliacoes)


class Serie(Video, Avaliavel):
    def __init__(self, titulo, ano_lancamento, resolucao, temporadas, episodios_por_temp):
        super().__init__(titulo, ano_lancamento, resolucao)
        self.temporadas = temporadas
        self.episodios_por_temp = episodios_por_temp
        self.avaliacoes = []

    def reproduzir(self):
        return f"Reproduzindo série '{self.titulo}' ({self.temporadas} temporadas) em {self.resolucao}."

    def tempo_total(self):
        # Considera média de 45 minutos por episódio
        return self.temporadas * self.episodios_por_temp * 45

    def avaliar(self, nota):
        self.avaliacoes.append(nota)
        return f"Série '{self.titulo}' avaliada com nota {nota}."

    def media_avaliacoes(self):
        if not self.avaliacoes:
            return 0.0
        return sum(self.avaliacoes) / len(self.avaliacoes)


class Musica(Audio, Baixavel):
    def __init__(self, titulo, ano_lancamento, autor, duracao_segundos):
        super().__init__(titulo, ano_lancamento, autor)
        self.duracao_segundos = duracao_segundos

    def reproduzir(self):
        return f"Tocando música '{self.titulo}' - {self.autor}."

    def tempo_total(self):
        return round(self.duracao_segundos / 60, 2)

    def baixar(self):
        return f"Download da música '{self.titulo}' concluído."

    def remover_download(self):
        return f"Download da música '{self.titulo}' removido."


class Podcast(Audio, Baixavel):
    def __init__(self, titulo, ano_lancamento, autor, episodio, duracao_minutos):
        super().__init__(titulo, ano_lancamento, autor)
        self.episodio = episodio
        self.duracao_minutos = duracao_minutos

    def reproduzir(self):
        return f"Ouvindo podcast '{self.titulo}' (Ep. {self.episodio}) por {self.autor}."

    def tempo_total(self):
        return self.duracao_minutos

    def baixar(self):
        return f"Download do episódio {self.episodio} de '{self.titulo}' concluído."

    def remover_download(self):
        return f"Download do episódio {self.episodio} de '{self.titulo}' removido."
