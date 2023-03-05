if exist env (
   echo "启动虚拟环境..."
   env\Scripts\activate.bat
) else (
   echo "不存在env目录，创建虚拟环境..."
   python -m venv env
   echo "启动虚拟环境..."
   env\Scripts\activate.bat
)
echo "安装依赖..."
pip install -r requirement.txt
echo "启动..."
python run.py
