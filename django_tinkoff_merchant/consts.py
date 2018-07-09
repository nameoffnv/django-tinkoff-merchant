TAXATION_OSN = 'osn'
TAXATION_USN_INCOME = 'usn_income'
TAXATION_USN_INCOME_OUTCOME = 'usn_income_outcome'
TAXATION_ENVD = 'envd'
TAXATION_ESN = 'esn'
TAXATION_PATENT = 'patent'

TAXATIONS = (
    (TAXATION_OSN, 'общая СН'),
    (TAXATION_USN_INCOME, 'упрощенная СН (доходы)'),
    (TAXATION_USN_INCOME_OUTCOME, 'упрощенная СН (доходы минус расходы)'),
    (TAXATION_ENVD, 'единый налог на вмененный доход'),
    (TAXATION_ESN, 'единый сельскохозяйственный налог'),
    (TAXATION_PATENT, 'патентная СН'),
)

TAX_ITEM_NONE = 'none'
TAX_ITEM_VAT0 = 'vat0'
TAX_ITEM_VAT10 = 'vat10'
TAX_ITEM_VAT18 = 'vat18'
TAX_ITEM_VAT110 = 'vat110'
TAX_ITEM_VAT118 = 'vat118'

TAXES = (
    (TAX_ITEM_NONE, 'без НДС'),
    (TAX_ITEM_VAT0, 'НДС по ставке 0%'),
    (TAX_ITEM_VAT10, 'НДС чека по ставке 10%'),
    (TAX_ITEM_VAT18, 'НДС чека по ставке 18%'),
    (TAX_ITEM_VAT110, 'НДС чека по расчетной ставке 10/110'),
    (TAX_ITEM_VAT118, 'НДС чека по расчетной ставке 18/118'),
)
