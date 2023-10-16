"""Book Value Per Share to Price."""

def book_price(common_equity_mr0: float,
               common_shares_outstanding_mr0: float,
               close: float,
               report_curr_to_usd: float, quote_curr_to_usd: float,
               ffill_limit: int = 0) -> float:
    r"""Book Value Per Share to Price.

    Notes:
        .. math::

            \begin{align}
            {BookToPrice}_n &= \frac
                {\frac{CommonEquity_n}{CommonSharesOutstanding_n}}
                {Close_n}
            \end{align}

    Args:
        common_equity_mr0 (float): book value of common equity.
        common_shares_outstanding_mr0 (float): shares outstanding.
        close (float): close price.
        quote_curr_to_usd (float): the quote currency to_usd conversion.
        report_curr_to_usd (float): the reporting currency to_usd conversion.
        ffill_limit (float): the number of days to forward fill by, uses
            ``pandas.Series.ffill``. The default behaviour is to not fill. NaNs
            that are not filled will generally be propagated forward.

    Returns:
        float: Book Value Per Share to Price.
    """
    if ffill_limit > 0:
        common_equity_ = common_equity_mr0.ffill(limit=ffill_limit)
        common_shares_outstanding_ = common_shares_outstanding_mr0 \
            .ffill(limit=ffill_limit)
        close_ = close.ffill(limit=ffill_limit)
    else:
        common_equity_ = common_equity_mr0.copy()
        common_shares_outstanding_ = common_shares_outstanding_mr0.copy()
        close_ = close.copy()

    bvps = safe_div(common_equity_ * report_curr_to_usd,
                    common_shares_outstanding_)
    close_ *= quote_curr_to_usd

    result = safe_div(bvps, close_)

    result.name = "BOOK_PRICE"
    result.category = CATEGORY

    return result