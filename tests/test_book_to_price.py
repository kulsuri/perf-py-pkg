"""Test cases for the book to price module."""
import pytest
from perf_py_pkg.value import book_to_price as btp

def test_book_price() -> None:
    """Test the book_price function."""
    # Sample data
    common_equity_mr0 = 1000.0
    common_shares_outstanding_mr0 = 100.0
    close = 10.0
    report_curr_to_usd = 2.0
    quote_curr_to_usd = 3.0

    result = btp.book_price(common_equity_mr0, common_shares_outstanding_mr0, close, 
                        report_curr_to_usd, quote_curr_to_usd)

    # Expected result calculation
    bvps = common_equity_mr0 * report_curr_to_usd / common_shares_outstanding_mr0
    expected_result = bvps / (close * quote_curr_to_usd)

    assert result == pytest.approx(expected_result)