all: clean parser model

parser: parser.py
model: model.py

parser.py: grammar.ebnf
	grako -o $@ $<

model.py: grammar.ebnf
	grako --object-model -o $@ $<

clean:
	rm -rf model.py parser.py
