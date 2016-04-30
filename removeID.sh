for ((i=1;i<11;i++))
do 
  cat data/user$i.py | cut -c 10 --complement > user$i.py
done

