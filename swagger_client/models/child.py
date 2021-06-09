# coding: utf-8

"""
    Swagger API2Cart

    API2Cart  # noqa: E501

    OpenAPI spec version: 1.1
    Contact: contact@api2cart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Child(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'parent_id': 'str',
        'sku': 'str',
        'upc': 'str',
        'ean': 'str',
        'mpn': 'str',
        'gtin': 'str',
        'sort_order': 'int',
        'created_time': 'A2CDateTime',
        'modified_time': 'A2CDateTime',
        'name': 'str',
        'short_description': 'str',
        'full_description': 'str',
        'images': 'list[Image]',
        'combination': 'list[ChildCombination]',
        'default_price': 'float',
        'cost_price': 'float',
        'list_price': 'float',
        'wholesale_price': 'float',
        'advanced_price': 'list[ProductAdvancedPrice]',
        'tax_class_id': 'str',
        'avail_for_sale': 'bool',
        'allow_backorders': 'bool',
        'in_stock': 'bool',
        'manage_stock': 'bool',
        'inventory_level': 'float',
        'inventory': 'list[ProductInventory]',
        'min_quantity': 'float',
        'default_qty_in_pack': 'float',
        'is_qty_in_pack_fixed': 'bool',
        'weight_unit': 'str',
        'weight': 'float',
        'dimensions_unit': 'str',
        'width': 'float',
        'height': 'float',
        'length': 'float',
        'additional_fields': 'object',
        'custom_fields': 'object'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parent_id',
        'sku': 'sku',
        'upc': 'upc',
        'ean': 'ean',
        'mpn': 'mpn',
        'gtin': 'gtin',
        'sort_order': 'sort_order',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'name': 'name',
        'short_description': 'short_description',
        'full_description': 'full_description',
        'images': 'images',
        'combination': 'combination',
        'default_price': 'default_price',
        'cost_price': 'cost_price',
        'list_price': 'list_price',
        'wholesale_price': 'wholesale_price',
        'advanced_price': 'advanced_price',
        'tax_class_id': 'tax_class_id',
        'avail_for_sale': 'avail_for_sale',
        'allow_backorders': 'allow_backorders',
        'in_stock': 'in_stock',
        'manage_stock': 'manage_stock',
        'inventory_level': 'inventory_level',
        'inventory': 'inventory',
        'min_quantity': 'min_quantity',
        'default_qty_in_pack': 'default_qty_in_pack',
        'is_qty_in_pack_fixed': 'is_qty_in_pack_fixed',
        'weight_unit': 'weight_unit',
        'weight': 'weight',
        'dimensions_unit': 'dimensions_unit',
        'width': 'width',
        'height': 'height',
        'length': 'length',
        'additional_fields': 'additional_fields',
        'custom_fields': 'custom_fields'
    }

    def __init__(self, id=None, parent_id=None, sku=None, upc=None, ean=None, mpn=None, gtin=None, sort_order=None, created_time=None, modified_time=None, name=None, short_description=None, full_description=None, images=None, combination=None, default_price=None, cost_price=None, list_price=None, wholesale_price=None, advanced_price=None, tax_class_id=None, avail_for_sale=None, allow_backorders=None, in_stock=None, manage_stock=None, inventory_level=None, inventory=None, min_quantity=None, default_qty_in_pack=None, is_qty_in_pack_fixed=None, weight_unit=None, weight=None, dimensions_unit=None, width=None, height=None, length=None, additional_fields=None, custom_fields=None):  # noqa: E501
        """Child - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._parent_id = None
        self._sku = None
        self._upc = None
        self._ean = None
        self._mpn = None
        self._gtin = None
        self._sort_order = None
        self._created_time = None
        self._modified_time = None
        self._name = None
        self._short_description = None
        self._full_description = None
        self._images = None
        self._combination = None
        self._default_price = None
        self._cost_price = None
        self._list_price = None
        self._wholesale_price = None
        self._advanced_price = None
        self._tax_class_id = None
        self._avail_for_sale = None
        self._allow_backorders = None
        self._in_stock = None
        self._manage_stock = None
        self._inventory_level = None
        self._inventory = None
        self._min_quantity = None
        self._default_qty_in_pack = None
        self._is_qty_in_pack_fixed = None
        self._weight_unit = None
        self._weight = None
        self._dimensions_unit = None
        self._width = None
        self._height = None
        self._length = None
        self._additional_fields = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_id is not None:
            self.parent_id = parent_id
        if sku is not None:
            self.sku = sku
        if upc is not None:
            self.upc = upc
        if ean is not None:
            self.ean = ean
        if mpn is not None:
            self.mpn = mpn
        if gtin is not None:
            self.gtin = gtin
        if sort_order is not None:
            self.sort_order = sort_order
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        if name is not None:
            self.name = name
        if short_description is not None:
            self.short_description = short_description
        if full_description is not None:
            self.full_description = full_description
        if images is not None:
            self.images = images
        if combination is not None:
            self.combination = combination
        if default_price is not None:
            self.default_price = default_price
        if cost_price is not None:
            self.cost_price = cost_price
        if list_price is not None:
            self.list_price = list_price
        if wholesale_price is not None:
            self.wholesale_price = wholesale_price
        if advanced_price is not None:
            self.advanced_price = advanced_price
        if tax_class_id is not None:
            self.tax_class_id = tax_class_id
        if avail_for_sale is not None:
            self.avail_for_sale = avail_for_sale
        if allow_backorders is not None:
            self.allow_backorders = allow_backorders
        if in_stock is not None:
            self.in_stock = in_stock
        if manage_stock is not None:
            self.manage_stock = manage_stock
        if inventory_level is not None:
            self.inventory_level = inventory_level
        if inventory is not None:
            self.inventory = inventory
        if min_quantity is not None:
            self.min_quantity = min_quantity
        if default_qty_in_pack is not None:
            self.default_qty_in_pack = default_qty_in_pack
        if is_qty_in_pack_fixed is not None:
            self.is_qty_in_pack_fixed = is_qty_in_pack_fixed
        if weight_unit is not None:
            self.weight_unit = weight_unit
        if weight is not None:
            self.weight = weight
        if dimensions_unit is not None:
            self.dimensions_unit = dimensions_unit
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if length is not None:
            self.length = length
        if additional_fields is not None:
            self.additional_fields = additional_fields
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this Child.  # noqa: E501


        :return: The id of this Child.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Child.


        :param id: The id of this Child.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this Child.  # noqa: E501


        :return: The parent_id of this Child.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Child.


        :param parent_id: The parent_id of this Child.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def sku(self):
        """Gets the sku of this Child.  # noqa: E501


        :return: The sku of this Child.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this Child.


        :param sku: The sku of this Child.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def upc(self):
        """Gets the upc of this Child.  # noqa: E501


        :return: The upc of this Child.  # noqa: E501
        :rtype: str
        """
        return self._upc

    @upc.setter
    def upc(self, upc):
        """Sets the upc of this Child.


        :param upc: The upc of this Child.  # noqa: E501
        :type: str
        """

        self._upc = upc

    @property
    def ean(self):
        """Gets the ean of this Child.  # noqa: E501


        :return: The ean of this Child.  # noqa: E501
        :rtype: str
        """
        return self._ean

    @ean.setter
    def ean(self, ean):
        """Sets the ean of this Child.


        :param ean: The ean of this Child.  # noqa: E501
        :type: str
        """

        self._ean = ean

    @property
    def mpn(self):
        """Gets the mpn of this Child.  # noqa: E501


        :return: The mpn of this Child.  # noqa: E501
        :rtype: str
        """
        return self._mpn

    @mpn.setter
    def mpn(self, mpn):
        """Sets the mpn of this Child.


        :param mpn: The mpn of this Child.  # noqa: E501
        :type: str
        """

        self._mpn = mpn

    @property
    def gtin(self):
        """Gets the gtin of this Child.  # noqa: E501


        :return: The gtin of this Child.  # noqa: E501
        :rtype: str
        """
        return self._gtin

    @gtin.setter
    def gtin(self, gtin):
        """Sets the gtin of this Child.


        :param gtin: The gtin of this Child.  # noqa: E501
        :type: str
        """

        self._gtin = gtin

    @property
    def sort_order(self):
        """Gets the sort_order of this Child.  # noqa: E501


        :return: The sort_order of this Child.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this Child.


        :param sort_order: The sort_order of this Child.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def created_time(self):
        """Gets the created_time of this Child.  # noqa: E501


        :return: The created_time of this Child.  # noqa: E501
        :rtype: A2CDateTime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Child.


        :param created_time: The created_time of this Child.  # noqa: E501
        :type: A2CDateTime
        """

        self._created_time = created_time

    @property
    def modified_time(self):
        """Gets the modified_time of this Child.  # noqa: E501


        :return: The modified_time of this Child.  # noqa: E501
        :rtype: A2CDateTime
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this Child.


        :param modified_time: The modified_time of this Child.  # noqa: E501
        :type: A2CDateTime
        """

        self._modified_time = modified_time

    @property
    def name(self):
        """Gets the name of this Child.  # noqa: E501


        :return: The name of this Child.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Child.


        :param name: The name of this Child.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_description(self):
        """Gets the short_description of this Child.  # noqa: E501


        :return: The short_description of this Child.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this Child.


        :param short_description: The short_description of this Child.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def full_description(self):
        """Gets the full_description of this Child.  # noqa: E501


        :return: The full_description of this Child.  # noqa: E501
        :rtype: str
        """
        return self._full_description

    @full_description.setter
    def full_description(self, full_description):
        """Sets the full_description of this Child.


        :param full_description: The full_description of this Child.  # noqa: E501
        :type: str
        """

        self._full_description = full_description

    @property
    def images(self):
        """Gets the images of this Child.  # noqa: E501


        :return: The images of this Child.  # noqa: E501
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this Child.


        :param images: The images of this Child.  # noqa: E501
        :type: list[Image]
        """

        self._images = images

    @property
    def combination(self):
        """Gets the combination of this Child.  # noqa: E501


        :return: The combination of this Child.  # noqa: E501
        :rtype: list[ChildCombination]
        """
        return self._combination

    @combination.setter
    def combination(self, combination):
        """Sets the combination of this Child.


        :param combination: The combination of this Child.  # noqa: E501
        :type: list[ChildCombination]
        """

        self._combination = combination

    @property
    def default_price(self):
        """Gets the default_price of this Child.  # noqa: E501


        :return: The default_price of this Child.  # noqa: E501
        :rtype: float
        """
        return self._default_price

    @default_price.setter
    def default_price(self, default_price):
        """Sets the default_price of this Child.


        :param default_price: The default_price of this Child.  # noqa: E501
        :type: float
        """

        self._default_price = default_price

    @property
    def cost_price(self):
        """Gets the cost_price of this Child.  # noqa: E501


        :return: The cost_price of this Child.  # noqa: E501
        :rtype: float
        """
        return self._cost_price

    @cost_price.setter
    def cost_price(self, cost_price):
        """Sets the cost_price of this Child.


        :param cost_price: The cost_price of this Child.  # noqa: E501
        :type: float
        """

        self._cost_price = cost_price

    @property
    def list_price(self):
        """Gets the list_price of this Child.  # noqa: E501


        :return: The list_price of this Child.  # noqa: E501
        :rtype: float
        """
        return self._list_price

    @list_price.setter
    def list_price(self, list_price):
        """Sets the list_price of this Child.


        :param list_price: The list_price of this Child.  # noqa: E501
        :type: float
        """

        self._list_price = list_price

    @property
    def wholesale_price(self):
        """Gets the wholesale_price of this Child.  # noqa: E501


        :return: The wholesale_price of this Child.  # noqa: E501
        :rtype: float
        """
        return self._wholesale_price

    @wholesale_price.setter
    def wholesale_price(self, wholesale_price):
        """Sets the wholesale_price of this Child.


        :param wholesale_price: The wholesale_price of this Child.  # noqa: E501
        :type: float
        """

        self._wholesale_price = wholesale_price

    @property
    def advanced_price(self):
        """Gets the advanced_price of this Child.  # noqa: E501


        :return: The advanced_price of this Child.  # noqa: E501
        :rtype: list[ProductAdvancedPrice]
        """
        return self._advanced_price

    @advanced_price.setter
    def advanced_price(self, advanced_price):
        """Sets the advanced_price of this Child.


        :param advanced_price: The advanced_price of this Child.  # noqa: E501
        :type: list[ProductAdvancedPrice]
        """

        self._advanced_price = advanced_price

    @property
    def tax_class_id(self):
        """Gets the tax_class_id of this Child.  # noqa: E501


        :return: The tax_class_id of this Child.  # noqa: E501
        :rtype: str
        """
        return self._tax_class_id

    @tax_class_id.setter
    def tax_class_id(self, tax_class_id):
        """Sets the tax_class_id of this Child.


        :param tax_class_id: The tax_class_id of this Child.  # noqa: E501
        :type: str
        """

        self._tax_class_id = tax_class_id

    @property
    def avail_for_sale(self):
        """Gets the avail_for_sale of this Child.  # noqa: E501


        :return: The avail_for_sale of this Child.  # noqa: E501
        :rtype: bool
        """
        return self._avail_for_sale

    @avail_for_sale.setter
    def avail_for_sale(self, avail_for_sale):
        """Sets the avail_for_sale of this Child.


        :param avail_for_sale: The avail_for_sale of this Child.  # noqa: E501
        :type: bool
        """

        self._avail_for_sale = avail_for_sale

    @property
    def allow_backorders(self):
        """Gets the allow_backorders of this Child.  # noqa: E501


        :return: The allow_backorders of this Child.  # noqa: E501
        :rtype: bool
        """
        return self._allow_backorders

    @allow_backorders.setter
    def allow_backorders(self, allow_backorders):
        """Sets the allow_backorders of this Child.


        :param allow_backorders: The allow_backorders of this Child.  # noqa: E501
        :type: bool
        """

        self._allow_backorders = allow_backorders

    @property
    def in_stock(self):
        """Gets the in_stock of this Child.  # noqa: E501


        :return: The in_stock of this Child.  # noqa: E501
        :rtype: bool
        """
        return self._in_stock

    @in_stock.setter
    def in_stock(self, in_stock):
        """Sets the in_stock of this Child.


        :param in_stock: The in_stock of this Child.  # noqa: E501
        :type: bool
        """

        self._in_stock = in_stock

    @property
    def manage_stock(self):
        """Gets the manage_stock of this Child.  # noqa: E501


        :return: The manage_stock of this Child.  # noqa: E501
        :rtype: bool
        """
        return self._manage_stock

    @manage_stock.setter
    def manage_stock(self, manage_stock):
        """Sets the manage_stock of this Child.


        :param manage_stock: The manage_stock of this Child.  # noqa: E501
        :type: bool
        """

        self._manage_stock = manage_stock

    @property
    def inventory_level(self):
        """Gets the inventory_level of this Child.  # noqa: E501


        :return: The inventory_level of this Child.  # noqa: E501
        :rtype: float
        """
        return self._inventory_level

    @inventory_level.setter
    def inventory_level(self, inventory_level):
        """Sets the inventory_level of this Child.


        :param inventory_level: The inventory_level of this Child.  # noqa: E501
        :type: float
        """

        self._inventory_level = inventory_level

    @property
    def inventory(self):
        """Gets the inventory of this Child.  # noqa: E501


        :return: The inventory of this Child.  # noqa: E501
        :rtype: list[ProductInventory]
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        """Sets the inventory of this Child.


        :param inventory: The inventory of this Child.  # noqa: E501
        :type: list[ProductInventory]
        """

        self._inventory = inventory

    @property
    def min_quantity(self):
        """Gets the min_quantity of this Child.  # noqa: E501


        :return: The min_quantity of this Child.  # noqa: E501
        :rtype: float
        """
        return self._min_quantity

    @min_quantity.setter
    def min_quantity(self, min_quantity):
        """Sets the min_quantity of this Child.


        :param min_quantity: The min_quantity of this Child.  # noqa: E501
        :type: float
        """

        self._min_quantity = min_quantity

    @property
    def default_qty_in_pack(self):
        """Gets the default_qty_in_pack of this Child.  # noqa: E501


        :return: The default_qty_in_pack of this Child.  # noqa: E501
        :rtype: float
        """
        return self._default_qty_in_pack

    @default_qty_in_pack.setter
    def default_qty_in_pack(self, default_qty_in_pack):
        """Sets the default_qty_in_pack of this Child.


        :param default_qty_in_pack: The default_qty_in_pack of this Child.  # noqa: E501
        :type: float
        """

        self._default_qty_in_pack = default_qty_in_pack

    @property
    def is_qty_in_pack_fixed(self):
        """Gets the is_qty_in_pack_fixed of this Child.  # noqa: E501


        :return: The is_qty_in_pack_fixed of this Child.  # noqa: E501
        :rtype: bool
        """
        return self._is_qty_in_pack_fixed

    @is_qty_in_pack_fixed.setter
    def is_qty_in_pack_fixed(self, is_qty_in_pack_fixed):
        """Sets the is_qty_in_pack_fixed of this Child.


        :param is_qty_in_pack_fixed: The is_qty_in_pack_fixed of this Child.  # noqa: E501
        :type: bool
        """

        self._is_qty_in_pack_fixed = is_qty_in_pack_fixed

    @property
    def weight_unit(self):
        """Gets the weight_unit of this Child.  # noqa: E501


        :return: The weight_unit of this Child.  # noqa: E501
        :rtype: str
        """
        return self._weight_unit

    @weight_unit.setter
    def weight_unit(self, weight_unit):
        """Sets the weight_unit of this Child.


        :param weight_unit: The weight_unit of this Child.  # noqa: E501
        :type: str
        """

        self._weight_unit = weight_unit

    @property
    def weight(self):
        """Gets the weight of this Child.  # noqa: E501


        :return: The weight of this Child.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Child.


        :param weight: The weight of this Child.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def dimensions_unit(self):
        """Gets the dimensions_unit of this Child.  # noqa: E501


        :return: The dimensions_unit of this Child.  # noqa: E501
        :rtype: str
        """
        return self._dimensions_unit

    @dimensions_unit.setter
    def dimensions_unit(self, dimensions_unit):
        """Sets the dimensions_unit of this Child.


        :param dimensions_unit: The dimensions_unit of this Child.  # noqa: E501
        :type: str
        """

        self._dimensions_unit = dimensions_unit

    @property
    def width(self):
        """Gets the width of this Child.  # noqa: E501


        :return: The width of this Child.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Child.


        :param width: The width of this Child.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this Child.  # noqa: E501


        :return: The height of this Child.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Child.


        :param height: The height of this Child.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def length(self):
        """Gets the length of this Child.  # noqa: E501


        :return: The length of this Child.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Child.


        :param length: The length of this Child.  # noqa: E501
        :type: float
        """

        self._length = length

    @property
    def additional_fields(self):
        """Gets the additional_fields of this Child.  # noqa: E501


        :return: The additional_fields of this Child.  # noqa: E501
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this Child.


        :param additional_fields: The additional_fields of this Child.  # noqa: E501
        :type: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Child.  # noqa: E501


        :return: The custom_fields of this Child.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Child.


        :param custom_fields: The custom_fields of this Child.  # noqa: E501
        :type: object
        """

        self._custom_fields = custom_fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Child, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Child):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other