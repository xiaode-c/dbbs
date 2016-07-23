# coding:utf-8


from django import template
from django.utils.html import mark_safe

register = template.Library()

def tree_search(d_dic, comment):
    for k, v_dic in d_dic.items():
        if k == comment.parent_comment:
            d_dic[k][comment] = {}
            return
        else:  # go deep
            tree_search(d_dic[k], comment)

def generate_comment_html(sub_comment_dic, margin_left_val):
    html = u""
    for k, v_dic in sub_comment_dic.items():
        html += child_node % (margin_left_val,  k.user.user_img.url, k.user.name, k.pub_date.ctime(), k.comment, k.id)
        if v_dic:
            html += generate_comment_html(v_dic, margin_left_val+50)
    return html


child_node = u'''<div style='margin-left:%spx;' class='comment-node'>
                    <div class='row'>
                        <div class='col-md-2'>
                            <img class='user-img' src='%s'>
                        </div>
                        <div class='col-md-10'>
                            <p>
                                <span class='username'>%s</span>
                                <span class='pub-date'>%s</span>
                            </p>
                            <p>%s</p>
                            <a class='reply' href='#comment-box' value='%s'>回复</a>
                        </div>
                    </div>
                </div>'''


parent_node = u'''<div class='comment-node'>
                    <div class='row'>
                        <div class='col-md-2'>
                            <img class='user-img' src='%s' />
                        </div>
                        <div class='col-md-10'>
                            <p>
                                <span class='username'>%s</span>
                                <span class='pub-date'>%s</span>
                            </p>
                            <p>%s</p>
                            <a class='reply' href='#comment-box' value='%s'>回复</a>
                        </div>
                    </div>
        </div>''' 



# build comment tree
@register.simple_tag
def build_comment_tree(comment_list):
    comment_dic = {}
    for comment in comment_list:
        if comment.parent_comment is None: #no parent
            comment_dic[comment] = {}
        else: # find father
            tree_search(comment_dic, comment)
    
    html = "<div class='comment-box'>"
    for k, v in comment_dic.items():
        html += parent_node % (k.user.user_img.url, k.user.name, k.pub_date.ctime(), k.comment, k.id)
        html += generate_comment_html(v, 50)
    # html += "</div>"
    return mark_safe(html)


