�
m>Rc           @   sC   d  �  Z  d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d S(   c         C   s   |  j  d � } | S(   s)   This function will break up words for us.t    (   t   split(   t   stufft   words(    (    s   ex25.pyt   break_words   s    c         C   s
   t  |  � S(   s   sorts the words.(   t   sorted(   R   (    (    s   ex25.pyt
   sort_words   s    c         C   s   |  j  d � } | GHd S(   s+   Prints the first word after popping it off.i    N(   t   pop(   R   t   word(    (    s   ex25.pyt   print_first_word
   s    c         C   s   |  j  d � } | GHd S(   s*   Prints the last word after popping it off.i����N(   R   (   R   R   (    (    s   ex25.pyt   print_last_word   s    c         C   s   t  |  � } t | � S(   s5   Takes in a full sentence and return the sorted words.(   R   R   (   t   sentenceR   (    (    s   ex25.pyt   sort_sentence   s    c         C   s$   t  |  � } t | � t | � d S(   s1   "Prints the first and last words of the sentence.N(   R   R	   R
   (   R   R   (    (    s   ex25.pyt   print_first_and_last   s    
c         C   s$   t  |  � } t | � t | � d S(   s3   Sorts the words then prints the first and last one.N(   R   R	   R
   (   R   R   (    (    s   ex25.pyt   print_first_and_last_sorted   s    
N(   R   R   R	   R
   R   R   R   (    (    (    s   ex25.pyt   <module>   s   						