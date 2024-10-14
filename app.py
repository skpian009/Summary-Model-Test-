# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("summarization", model="Falconsai/medical_summarization")

result =""" Pimples, or acne, are a common skin issue caused by clogged pores from oil, dead skin cells, and bacteria. While many turn to medications, natural remedies can be equally effective in treating and preventing pimples. Here are simple and drug-free ways to clear your skin.

1. Cleanse Regularly:
Wash your face twice daily with a gentle cleanser to remove dirt and oil. Avoid over-washing as it can strip the skin’s natural oils, causing more oil production and potential breakouts.

2. Exfoliate Gently:
Exfoliating once or twice a week removes dead skin cells that clog pores. Opt for natural exfoliants like oatmeal or sugar to prevent irritation.

3. Avoid Touching Your Face:
Hands transfer bacteria and dirt to the skin. Avoid picking or squeezing pimples to prevent infections and scarring.

4. Natural Spot Treatments:

Tea Tree Oil: Its antibacterial properties reduce inflammation. Dilute and apply directly to the pimple.
Aloe Vera: It soothes irritated skin and helps heal acne.
Honey and Cinnamon: This antibacterial mask helps prevent further breakouts.
Green Tea: Rich in antioxidants, applying it topically reduces inflammation, while drinking it helps detox the body.
5. Maintain a Healthy Diet:
Reduce sugary and processed foods, as they can trigger acne. Incorporate fruits, vegetables, and omega-3 rich foods like fish to promote clearer skin.

6. Stay Hydrated and Manage Stress:
Drink plenty of water to flush out toxins and maintain skin hydration. Practice relaxation techniques to manage stress, which can cause acne flare-ups.

These simple, natural methods can help you remove pimples without medications, promoting clearer and healthier skin"""

prompt = pipe(f"""{result}""")
print(prompt)
