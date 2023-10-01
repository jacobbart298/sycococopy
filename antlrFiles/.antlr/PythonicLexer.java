// Generated from c:\Users\User\OneDrive\Documenten\Open Universiteit\IB9902 Voorbereiden Afstuderen\sycococopy\antlrFiles\Pythonic.g4 by ANTLR 4.9.2

from antlr_denter.DenterHelper import DenterHelper
from PythonicParser import PythonicParser

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class PythonicLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROTOCOL=1, ROLES=2, TO=3, FROM=4, SEND=5, SEQUENCE=6, SHUFFLE=7, CHOICE=8, 
		REPEAT=9, LOOP=10, CLOSE=11, WORD=12, WS=13, NL=14;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", "CHOICE", 
			"REPEAT", "LOOP", "CLOSE", "WORD", "WS", "NL"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'protocol:'", "'roles:'", "'to'", "'from'", "'send'", "'sequence:'", 
			"'shuffle:'", "'choice:'", "'repeat'", "'loop'", "'close'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", 
			"CHOICE", "REPEAT", "LOOP", "CLOSE", "WORD", "WS", "NL"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	class MyCoolDenter(DenterHelper):
	    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
	        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
	        self.lexer: PythonicLexer = lexer

	    def pull_token(self):
	        return super(PythonicLexer, self.lexer).nextToken()

	denter = None

	def nextToken(self):
	    if not self.denter:
	        self.denter = self.MyCoolDenter(self, self.NL, PythonicParser.INDENT, PythonicParser.DEDENT, False)
	    return self.denter.next_token()



	public PythonicLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Pythonic.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20}\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5"+
		"\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r"+
		"\6\rl\n\r\r\r\16\rm\3\16\3\16\3\16\3\16\3\17\5\17u\n\17\3\17\3\17\7\17"+
		"y\n\17\f\17\16\17|\13\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23"+
		"\13\25\f\27\r\31\16\33\17\35\20\3\2\3\6\2\62;C\\aac|\2\177\2\3\3\2\2\2"+
		"\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2"+
		"\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2"+
		"\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5)\3\2\2\2\7\60\3\2\2\2\t\63\3"+
		"\2\2\2\138\3\2\2\2\r=\3\2\2\2\17G\3\2\2\2\21P\3\2\2\2\23X\3\2\2\2\25_"+
		"\3\2\2\2\27d\3\2\2\2\31k\3\2\2\2\33o\3\2\2\2\35t\3\2\2\2\37 \7r\2\2 !"+
		"\7t\2\2!\"\7q\2\2\"#\7v\2\2#$\7q\2\2$%\7e\2\2%&\7q\2\2&\'\7n\2\2\'(\7"+
		"<\2\2(\4\3\2\2\2)*\7t\2\2*+\7q\2\2+,\7n\2\2,-\7g\2\2-.\7u\2\2./\7<\2\2"+
		"/\6\3\2\2\2\60\61\7v\2\2\61\62\7q\2\2\62\b\3\2\2\2\63\64\7h\2\2\64\65"+
		"\7t\2\2\65\66\7q\2\2\66\67\7o\2\2\67\n\3\2\2\289\7u\2\29:\7g\2\2:;\7p"+
		"\2\2;<\7f\2\2<\f\3\2\2\2=>\7u\2\2>?\7g\2\2?@\7s\2\2@A\7w\2\2AB\7g\2\2"+
		"BC\7p\2\2CD\7e\2\2DE\7g\2\2EF\7<\2\2F\16\3\2\2\2GH\7u\2\2HI\7j\2\2IJ\7"+
		"w\2\2JK\7h\2\2KL\7h\2\2LM\7n\2\2MN\7g\2\2NO\7<\2\2O\20\3\2\2\2PQ\7e\2"+
		"\2QR\7j\2\2RS\7q\2\2ST\7k\2\2TU\7e\2\2UV\7g\2\2VW\7<\2\2W\22\3\2\2\2X"+
		"Y\7t\2\2YZ\7g\2\2Z[\7r\2\2[\\\7g\2\2\\]\7c\2\2]^\7v\2\2^\24\3\2\2\2_`"+
		"\7n\2\2`a\7q\2\2ab\7q\2\2bc\7r\2\2c\26\3\2\2\2de\7e\2\2ef\7n\2\2fg\7q"+
		"\2\2gh\7u\2\2hi\7g\2\2i\30\3\2\2\2jl\t\2\2\2kj\3\2\2\2lm\3\2\2\2mk\3\2"+
		"\2\2mn\3\2\2\2n\32\3\2\2\2op\7\"\2\2pq\3\2\2\2qr\b\16\2\2r\34\3\2\2\2"+
		"su\7\17\2\2ts\3\2\2\2tu\3\2\2\2uv\3\2\2\2vz\7\f\2\2wy\7\"\2\2xw\3\2\2"+
		"\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\36\3\2\2\2|z\3\2\2\2\7\2kmtz\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}