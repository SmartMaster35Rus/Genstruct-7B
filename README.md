# Genstruct-7B //beta-test

Представляет собой модель генерации инструкций, разработанную для создания действительных инструкций на основе исходного текстового корпуса. 

Эта модель позволяет создавать новые, частично синтетические наборы данных для донастройки инструкций из любого текстового корпуса. 

Для использования данного репозитория вам необходимо загрузить модель и токенизатор, а затем можно приступить к генерации инструкций.

# command 

``` terminal conda 

conda create -n Genstruct python=3.10  // создаем наше отдельное виртуальное окружение обязательно python 3.10 [3.12/3.11 not working]
conda activate Genstruct // активируем наше виртуальное окружение 
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch // для работы cuda
pip install transformers 
pip install autoawq // !!! найти точную версию для установки !!!
pip install jupyter notebook //для завода связки GPU
pip install tensorflow // для связки с jupyter + tensorflow = GPU[0]:true

проверяем работу tensorflow GPU:

import tensorflow as Genstruct
gpus = Genstruct.config.experimental.list_physical_devices('GPU*)
print (gpus)

```

