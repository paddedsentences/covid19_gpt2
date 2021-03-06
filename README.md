# covid19

Finetuning GPT-2 on [Allen Institute Covid19 dataset](https://allenai.org/data/cord-19) to generate text about the recent scientific literature. Ideally the goal is to make an automatic scientist. If it is first finetuned on a larger scientific dataset and then finetuned on the covid19 dataset the connections that the algorithm would make would be more interesting.

# how to use this code
1. clone the repository with `git clone https://github.com/LuCeHe/covid19_gpt2`, get inside the folder and run `pip install -r requirements.txt`
2. run `reformat_data.py` to download the dataset and reformat it in the proper way to use [HuggingFace](https://huggingface.co/) library
3. run the following command for finetuning gpt2: 

```pythonscript
python run_language_modeling.py --output_dir=output --model_type=gpt2 --model_name_or_path=gpt2-xl --do_train --train_data_file=data/covid19.txt --do_eval --eval_data_file=data/small_covid19.txt --overwrite_output_dir --block_size=200 --per_gpu_train_batch_size=4 --save_steps 200000 --num_train_epochs=1
```

4. run the following command for generating samples from the finetuned model: 

```pythonscript
python run_generation.py --model_type=gpt2 --model_name_or_path=output --k=10 --length=200 --num_return_sequences=4 --prompt="The reason why covid19 finished"
```
```pythonscript
python run_generation.py --model_type=gpt2 --model_name_or_path=output --k=10 --length=200 --num_return_sequences=4 --prompt="An effective vaccine against covid19"
```
```pythonscript
python run_generation.py --model_type=gpt2 --model_name_or_path=output --k=10 --length=200 --num_return_sequences=4 --prompt="The frequency in the X-rays for optimally breaking covid19"
```

# interesting samples

The outputs are still repetitive and not very informative. However I will put here the ones I found to be more interesting and the code used for generating it.

## sample 1

```pythonscript
python run_language_modeling.py --output_dir=output --model_type=gpt2 --model_name_or_path=gpt2-medium --do_train --train_data_file=data/covid19.txt --do_eval --eval_data_file=data/small_covid19.txt --overwrite_output_dir --block_size=200 --per_gpu_train_batch_size=4 --save_steps 200000 --num_train_epochs=1
python run_generation.py --model_type=gpt2 --model_name_or_path=output --k=10 --length=200 --num_return_sequences=3 --prompt="The reason why covid19 finished"
```

=== GENERATED SEQUENCE 3 ===

The reason why covid19 finished as the top 10 was not clear. It is possible that it was a result of the fact that many of the participants were not in the hospital and/or had to go home for other reasons. We cannot rule out the possibility of an effect due to the small number of people who were infected and/or the fact that the participants were in hospital for longer than 5 days.

Discussion

We conducted this study with a small sample size of a small sample of individuals, with a relatively large number of participants and with the aim of developing an evidence-based approach to the management of COVID-19. The findings of this study support the recommendations of the Chinese Government and WHO, which have emphasized the importance of rapid diagnosis and isolation of patients who are infected with COVID-19.The findings of this study show that the use of personal protective equipment (PPE) and contact precautions is the key to reducing the number of cases and deaths. In particular, the use of a mask

## sample 2

```pythonscript
python run_language_modeling.py --output_dir=output --model_type=gpt2 --model_name_or_path=gpt2-medium --do_train --train_data_file=data/covid19.txt --do_eval --eval_data_file=data/small_covid19.txt --overwrite_output_dir --block_size=200 --per_gpu_train_batch_size=4 --save_steps 200000 --num_train_epochs=1
python run_generation.py --model_type=gpt2 --model_name_or_path=output --k=20 --length=400 --num_return_sequences=3 --prompt="The most effective vaccine for covid19"
```

=== GENERATED SEQUENCE 2 ===

The most effective vaccine for covid19, the rRBD-based vaccine, is in phase II/III trials, but there are still concerns about its safety. To address these concerns, we used a live attenuated virus (strain SZ16) to express the RBD in a replication-defective (RdRp) form and inactivated it at high temperatures for 10 min. This was followed by a booster dose of SZ16 and a boost with the rRBD. The SZ16 vaccine did not induce neutralizing antibodies and was found to elicit both systemic and mucosal immunity. It is the first RBD-based vaccine for COVID-19, and the rRBD-based vaccine is the first live attenuated vaccine for SARS-CoV and MERS-CoV.

Introduction

In December 2019, a new coronavirus pneumonia was identified in Wuhan, China. It was named as a novel coronavirus (2019-nCoV), and it was rapidly identified in patients from Wuhan. By July 10, 2020, it had spread across the world, infecting over 27 countries in the world, and causing over 8,400 deaths [1]. In the disease caused by 2019-nCoV was named as severe acute respiratory syndrome, and it is highly contagious, with more than 80 % of cases were reported as pneumonia, and more than 10,000 cases died in the USA and China [2]. It is caused the largest ever epidemic outbreak in human respiratory diseases, and the mortality rate of 2019-nCoVirus (HCoV is about 40-related disease has exceeded that of the previous epidemic in China, and has been caused about 5, with the world's population in the last year [3]. The epidemic, and the number of people infected about 3, the world and the total number of infected by January 1. We found that was about 8,000, with the total is the


# other collections of scientific literature

- [The CORE Collection](https://core.ac.uk/services/#access-to-raw-data)
- [ArXiV collection](https://link.springer.com/article/10.1007/s11192-020-03382-z)
