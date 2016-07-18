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
    html = ""
    for k, v_dic in sub_comment_dic.items():
        html += "<div style='margin-left:%spx;' class='comment-node'><p><span class='username'>" \
                % margin_left_val + k.user.name + "</span><span class='pub-date'>" \
                + str(k.pub_date.ctime()) +"</span></p><p>"+ k.comment +"</p>" + "<a class='reply' href='#comment-box' value="\
                + str(k.id) +u">回复</a>" + "</div>"
        if v_dic:
            html += generate_comment_html(v_dic, margin_left_val+50)
    return html

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
        html += "<div class='comment-node'><p><span class='username'>"\
                + k.user.name + "</span><span class='pub-date'>"+ str(k.pub_date.ctime()) \
                +"</span></p><p>"+ k.comment +"</p>"+ "<a class='reply' href='#comment-box' value="\
                + str(k.id) +u">回复</a>" + "</div>"
        html += generate_comment_html(v, 50)
    html += "</div>"
    return mark_safe(html)
