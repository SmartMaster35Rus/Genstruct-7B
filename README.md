# Genstruct-7B //beta-test

Добро пожаловать в репозиторий Genstruct-7B //beta-test! Здесь вы найдете модель для генерации инструкций на основе текстового корпуса.

### Характеристики ПК
Данный скрипт был разработан и протестирован на следующей конфигурации ПК:

|  Конфигурация  |  Детали спецификаций  |
|----------------|----------------------|
|  Процессор     |  Intel® Core™ i9-14900KF @3.20Ghz  |
|  Память        |  128 ГБ DDR4 4200 МГц (32+32+32+32)  |
|  Диск          |  M.2 PCIe SSD Samsung SSD 980 PRO 1000 ГБ  |
|  Диск          |  M.2 PCIe SSD XPG GAMMIX S11 Pro 1000 ГБ |
|  Дискретная графика  |  NVIDIA GeForce RTX 4090 24 ГБ  |
|  Модель Whisper  |  Whisper Large-v3  |
|  CudaToolkit   |  ver.12.3  |
|  OS   |  Windows 11 Pro |

## Описание проекта

#Genstruct-7B 

//beta-test представляет собой модель генерации инструкций, разработанную для создания действительных инструкций на основе исходного текстового корпуса. Эта модель позволяет создавать новые, частично синтетические наборы данных для донастройки инструкций из любого текстового корпуса.

### !!!Важно: На данный момент данный репозиторий находится в бета-тесте.!!!


## Установка и настройка

Для начала работы с Genstruct-7B //beta-test, выполните следующие шаги:

### 1. Создание виртуального окружения

Для изоляции проекта рекомендуется создать новое виртуальное окружение. Выполните следующие команды в терминале:

```python
conda create -n Genstruct python=3.10
conda activate Genstruct
```

### 2. Установка зависимостей

Установите необходимые библиотеки, выполнив следующие команды:

## Верссии tensorflow выше 2.10 не работают на Windows поэтому ставим версию ниже 2.11

```python
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
pip install transformers
pip install torch --upgrade --index-url https://download.pytorch.org/whl/cu121
pip install xformers --upgrade --index-url https://download.pytorch.org/whl/cu121
pip install jupyter notebook
python -m pip install "tensorflow<2.11"
pip install autoawq
```

### 3. Проверка настройки TensorFlow GPU

Для использования GPU в TensorFlow, убедитесь, что настройка выполнена корректно. Выполните следующую команду:

```python
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

если все настроено правильно вы получаете ответ :

[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

### 4. Запуск Jupyter Notebook

Запустите Jupyter Notebook, чтобы проверить доступность GPU. Введите следующую команду в терминале:
```python
conda activate Genstruct ##активируем наше виртуальное окружение 
pip install ipykernel
python -m ipykernel install --user --name=Genstruct ##Добавляем наше окружение в Jupyter Notebook
jupyter notebook ##Откроется браузер сос тратовой страницей Jupyter Notebook 
```

Выберите виртуальное окружение Genstruct (сверху справа) в интерфейсе Jupyter Notebook и перейдите в него. 
Вводим команду:

```shell
import tensorflow as Genstruct
gpus = Genstruct.config.list_physical_devices('GPU')
print ( gpus )

```
Если все настроено правильно и GPU работает вы получаете ответ : 

```
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

### 5. Генерация инструкций

Теперь вы готовы к генерации инструкций с использованием модели Genstruct-7B //beta-test. Следуйте инструкциям и документации, чтобы получить желаемые результаты.

## Дополнительная информация

Дополнительные сведения и примеры использования можно найти в документации репозитория.

Мы надеемся, что Genstruct-7B //beta-test поможет вам создавать качественные инструкции и улучшит ваш опыт работы с текстовыми данными. Желаем вам успехов!
