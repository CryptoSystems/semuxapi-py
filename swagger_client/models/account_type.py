# coding: utf-8

"""
    Semux API

    Semux is an experimental high-performance blockchain platform that powers decentralized application.  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AccountType(object):
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
        'address': 'str',
        'available': 'str',
        'locked': 'str',
        'nonce': 'str',
        'transaction_count': 'int',
        'pending_transaction_count': 'int'
    }

    attribute_map = {
        'address': 'address',
        'available': 'available',
        'locked': 'locked',
        'nonce': 'nonce',
        'transaction_count': 'transactionCount',
        'pending_transaction_count': 'pendingTransactionCount'
    }

    def __init__(self, address=None, available=None, locked=None, nonce=None, transaction_count=None, pending_transaction_count=None):  # noqa: E501
        """AccountType - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._available = None
        self._locked = None
        self._nonce = None
        self._transaction_count = None
        self._pending_transaction_count = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if available is not None:
            self.available = available
        if locked is not None:
            self.locked = locked
        if nonce is not None:
            self.nonce = nonce
        if transaction_count is not None:
            self.transaction_count = transaction_count
        if pending_transaction_count is not None:
            self.pending_transaction_count = pending_transaction_count

    @property
    def address(self):
        """Gets the address of this AccountType.  # noqa: E501


        :return: The address of this AccountType.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AccountType.


        :param address: The address of this AccountType.  # noqa: E501
        :type: str
        """
        if address is not None and not re.search('^(0x)?[0-9a-fA-F]{40}$', address):  # noqa: E501
            raise ValueError("Invalid value for `address`, must be a follow pattern or equal to `/^(0x)?[0-9a-fA-F]{40}$/`")  # noqa: E501

        self._address = address

    @property
    def available(self):
        """Gets the available of this AccountType.  # noqa: E501


        :return: The available of this AccountType.  # noqa: E501
        :rtype: str
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this AccountType.


        :param available: The available of this AccountType.  # noqa: E501
        :type: str
        """
        if available is not None and not re.search('^\\d+$', available):  # noqa: E501
            raise ValueError("Invalid value for `available`, must be a follow pattern or equal to `/^\\d+$/`")  # noqa: E501

        self._available = available

    @property
    def locked(self):
        """Gets the locked of this AccountType.  # noqa: E501


        :return: The locked of this AccountType.  # noqa: E501
        :rtype: str
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this AccountType.


        :param locked: The locked of this AccountType.  # noqa: E501
        :type: str
        """
        if locked is not None and not re.search('^\\d+$', locked):  # noqa: E501
            raise ValueError("Invalid value for `locked`, must be a follow pattern or equal to `/^\\d+$/`")  # noqa: E501

        self._locked = locked

    @property
    def nonce(self):
        """Gets the nonce of this AccountType.  # noqa: E501


        :return: The nonce of this AccountType.  # noqa: E501
        :rtype: str
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this AccountType.


        :param nonce: The nonce of this AccountType.  # noqa: E501
        :type: str
        """
        if nonce is not None and not re.search('^\\d+$', nonce):  # noqa: E501
            raise ValueError("Invalid value for `nonce`, must be a follow pattern or equal to `/^\\d+$/`")  # noqa: E501

        self._nonce = nonce

    @property
    def transaction_count(self):
        """Gets the transaction_count of this AccountType.  # noqa: E501


        :return: The transaction_count of this AccountType.  # noqa: E501
        :rtype: int
        """
        return self._transaction_count

    @transaction_count.setter
    def transaction_count(self, transaction_count):
        """Sets the transaction_count of this AccountType.


        :param transaction_count: The transaction_count of this AccountType.  # noqa: E501
        :type: int
        """

        self._transaction_count = transaction_count

    @property
    def pending_transaction_count(self):
        """Gets the pending_transaction_count of this AccountType.  # noqa: E501


        :return: The pending_transaction_count of this AccountType.  # noqa: E501
        :rtype: int
        """
        return self._pending_transaction_count

    @pending_transaction_count.setter
    def pending_transaction_count(self, pending_transaction_count):
        """Sets the pending_transaction_count of this AccountType.


        :param pending_transaction_count: The pending_transaction_count of this AccountType.  # noqa: E501
        :type: int
        """

        self._pending_transaction_count = pending_transaction_count

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccountType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
