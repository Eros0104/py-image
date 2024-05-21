# Aplicativo de Filtros de Imagem

Este é um aplicativo de linha de comando que aplica filtros de imagem a uma imagem de entrada. Desenvolvido como parte da disciplina "Digital Image Processing & Machine Learning" do curso de Sistemas de Informação da Faculdade de Informática e Administração Paulista (FIAP).

## Requisitos

- Python 3
- OpenCV

Você pode instalar o OpenCV executando o seguinte comando:

```bash
pip install opencv-python
```

## Uso

O script utiliza argumentos de linha de comando para especificar a imagem de entrada, o filtro a ser aplicado e outros parâmetros. Abaixo está uma descrição dos argumentos disponíveis.

### Argumentos

#### Obrigatórios 
- --path: (Obrigatório) Caminho para a imagem de entrada.

#### Blur
- --blur: Tipo de filtro de desfoque a ser aplicado. As opções são **gaussian** ou **median**.
- --kernel: Tamanho do kernel para o filtro de desfoque. Por exemplo, --kernel 15 para um kernel de 15x15.
- --sigma: Desvio padrão do filtro de desfoque gaussiano.

#### Edge Detection
- --edge: Tipo de filtro de detecção de bordas a ser aplicado. Atualmente, apenas **canny** é suportado.

#### Transformada de Fourier
- --fourier: Tipo de filtro de Transformada de Fourier a ser aplicado. As opções são **low**, **high** ou **band**.

#### Outros
- --output: Caminho para salvar a imagem de saída.

### Exemplos

Aplicar um filtro de desfoque gaussiano com um kernel de 15x15:

```bash
python main.py --path input.jpg --blur gaussian --kernel 15 --output output.jpg
```

Aplicar um filtro de detecção de bordas Canny:

```bash
python main.py --path input.jpg --edge canny --output output.jpg
```

Aplicar um filtro de Transformada de Fourier passa-baixa:

```bash
python main.py --path input.jpg --fourier low --output output.jpg
```

### Makefile

O projeto inclui um arquivo Makefile para gerar múltiplas imagens de exemplo. Para gerar as imagens, execute o seguinte comando:

```bash
make
```