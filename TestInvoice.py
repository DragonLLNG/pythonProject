import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

@pytest.fixture()
def taxRate():
    taxRate = 10
    return taxRate



def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75


def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanCalculateTax(invoice, products, taxRate):
    invoice.calculateTax(products, taxRate)
    assert invoice.calculateTax(products, taxRate) == 6.94

def test_CanCalculateFinalPrice(invoice, products, taxRate):
    invoice.finalPrice(products, taxRate)
    assert invoice.finalPrice(products, taxRate) == 81.94