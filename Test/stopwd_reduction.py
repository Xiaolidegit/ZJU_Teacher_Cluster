# ͣ�ôʱ����н��д洢��ÿһ��ֻ��һ������
# ���������ռ�����ͣ�ôʱ�ȥ��
def stopwd_reduction(infilepath, outfilepath):
    infile = open(infilepath, 'r', encoding='utf-8')
    outfile = open(outfilepath, 'w')
    stopwordslist = []
    '''
        infile.read().split('\n')��
        read������ȡ�ı�����Ϊstr��ʽ��
        ��ͨ��split�������ַ���������Ƭ�������طָ����ַ����б�(list)
    '''
    for str in infile.read().split('\n'):
        if str not in stopwordslist:
            stopwordslist.append(str)
            outfile.write(str + '\n')


stopwd_reduction('./test/stopwords.txt', './test/stopword.txt')
