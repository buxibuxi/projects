
#微信公众号文章相似度分析

##数据结构

###思路
- 先找到每一篇文章的唯一编号，可以选择链接中的sn
- 建立每一篇文章的hash表，存储{文章标题、文章创建时间、阅读数、点赞数、是否有原创标识等}
- 同时建立一个集合，存储所有文章的唯一编号
- 相似度存储：


###数据结构
	- docid:(hashmap)	#存储每一篇文章的信息
		{account_name:; 
		account_id:
		ptime:;
		read_num:
		praise_num:
		isoriginal:
		src:(文章来源，初始化均为自己)
		srcmark:(待补充，从文章中爬取)
		}
	- docs:(set)	#存储所有文章的id
	- cheat_docs:(set) #存储所有抄袭文章组的根节点（源文章）
	- src_docid:(set)	#抄袭文章组，存储所有抄袭该文章的其他文章id 


