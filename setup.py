import os

os.system('pip install pygit2==1.12.2')
os.system('git clone https://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@github.com/llyasviel/Fooocus-git')
os.system('wget -O /content/Fooocus/models/upscale_models/fococus_upscaler_s4099855.bin https://huggingface.co/llyasviel/nisc/resolve/main/fococus_upscaler_s4099855.bin')
os.system('python /content/Fooocus/entry_with_update.py --share')
