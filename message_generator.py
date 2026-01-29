"""
Message Generator Module
Uses local LLM to generate natural negotiation messages
"""


def system_prompt():
    """Build system prompt for the LLM"""
    return """You are an expert negotiator helping someone make a fair offer on a Facebook Marketplace listing in the UK. 

Your task is to write a brief, friendly, and persuasive message to the seller. The message should:

1. Be conversational and respectful (150-200 words maximum)
2. Express genuine interest in the item
3. Mention 2-3 specific, factual concerns that justify a lower offer
4. Present a counter-offer with brief justification
5. Keep the tone positive and leave room for discussion
6. Use British English and reference prices in pounds (£)

AVOID:
- Being aggressive or demanding
- Making the seller feel insulted
- Obvious lowballing tactics that seem unreasonable
- Desperate language
- Over-explaining or being too wordy

The goal is to create a message that feels natural, as if written by a knowledgeable buyer who has done their research."""
    
def user_prompt():
    """Build user prompt with product and analysis data"""
    product_name = ('product_name', 'the item')
    asking_price = ('price', 0)

    prompt = f"""Write a negotiation message for this Facebook Marketplace listing:

PRODUCT: {product_name}
ASKING PRICE: £{asking_price:,.0f}

Write a natural, friendly message that incorporates these points without sounding scripted. Make it feel conversational."""
        
    return prompt
    