class Pager(object):
  def __init__(self,current_page):
    self.current_page = int(current_page)
    # self.size = int(size)
  #把方法伪造成属性(1)
  @property
  def start(self):
      return (self.current_page-1)*10
  @property
  def end(self):
      return self.current_page*10