# -*- coding: utf-8 -*- #su dung bo ma Unicode
from openerp.osv import fields,osv

class book (osv.osv):
    _name='book.book'
    _columns = {
        #cac thuoc tinh cua lop book
        'name':fields.char('Ten dien thoai', size=25, required=True, translate=True),
        'pages':fields.integer('Gia'),
        'origin of goods':fields.selection([('tt','Trung Quoc'),('tn','Han Quoc'),
                                 ('tth','My')],'Xuat xu'),
        'brand':fields.selection([('tt','Samsung'),('tn','Iphone'),
                                 ('tth','Redmi'),('th','Poco')],'Thuong hieu'),
        'published_date':fields.datetime('Ngay phat hanh'),
        'active':fields.boolean('Dang ban ?'),
        'notes':fields.text('Chi tiet')
    }
    _defaults={
        'pages':0,
        'active':True,
    }
book() #tao 1 the hien cho lop book_book
